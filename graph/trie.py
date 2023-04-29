ALP_SIZE = 26
class Node:
    def __init__(self):
        self.children = [None] * ALP_SIZE # 子を管理する配列
        self.word_endpoint = False # 根からこの頂点までの単語が存在するか
        self.matched_prefix_cnt = 0 # 同じ接頭辞を持つ単語の数

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        now = self.root
        for alp in word:
            idx = ord(alp) - ord('a')
            if now.children[idx] == None:
                now.children[idx] = Node()
            now = now.children[idx]
            now.matched_prefix_cnt += 1
        else:
            now.word_endpoint = True

    # (wordが含まれるか、wordを接頭辞に持つ単語の数)を返す
    def search(self, word):
        now = self.root
        for alp in word:
            idx = ord(alp) - ord('a')
            now = now.children[idx]
            if now == None:
                return False, 0
        else:
            return now.word_endpoint, now.matched_prefix_cnt
