class RMQ:
    def __init__(self, array):
        n = len(array)
        self.e = 1 << 30
        self.num = 1 << (n - 1).bit_length()
        self.tree = [(self.e, -1)] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = (array[i], i)

        for i in range(self.num - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x): # A[k] = x
        k += self.num
        self.tree[k] = (x, k) 
        while k > 1:
            self.tree[k >> 1] = min(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r): # [l, r)
        ret = (self.e, -1)
        l += self.num
        r += self.num

        while l < r:
            if l & 1:
                ret = min(ret, self.tree[l])
                l += 1
            if r & 1:
                ret = min(ret, self.tree[r - 1])
            l >>= 1
            r >>= 1
        
        idx = ret[1]
        assert idx >= 0
        return idx

class BIT:
    def __init__(self, N):
        self.N = N
        self.data = [0] * (N + 1)
        self.A = [0] * (N + 1)
        self.all_sum = 0
 
    def add(self, i, x):
        self.all_sum += x
        self.A[i] += x
        while i <= self.N:
            self.data[i] += x
            i += i & -i

    def update(self, i, x): self.add(i, x - self.A[i])

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.data[i]
            i -= i & -i
        return ret
    
    def range_sum(self, l, r): return self.sum(r) - self.sum(l - 1)

    def get(self, i): return self.A[i]
    
    def less_than_x(self, x): return self.lower_bound(self.sum(x))
    
    def more_than_x(self, x): return self.lower_bound(self.sum(x - 1) + 1)

    def lower_bound(self, w):
        if w <= 0: return None
        if w > self.get_all_sum(): return None
        i = 0
        size = 1 << self.N.bit_length()
        while size > 0:
            if i + size <= self.N and self.data[i + size] < w:
                w -= self.data[i + size]
                i += size 
            size >>= 1

        return i + 1

    def get_all_sum(self): return self.all_sum

    def print(self):
        print("[index]", " ".join(map(str, [i for i in range(1, self.N + 1)])))
        print("[value]", " ".join(map(str, [self.A[i] for i in range(1, self.N + 1)])))

class EulerTour:
    def __init__(self, N, node, vertex_cost = False):
        '''
        【コンストラクタ】
            node[v] = [(nx, i), ...] vとnxにコストiの辺を張る
            vertex_cost[v] = a 頂点vにコストaを与える

        【メソッド】
            lca(u, v)                 : u, vの最近共通祖先
            root_path_edge_length(v)  : 根からxまでの距離を求める
            root_path_vertex_cost(v)  : 根からxまでの頂点のコストの総和を求める
            uv_path_edge_length(u, v) : uからvまでの距離を求める
            uv_path_vertex_cost(u, v) : uからvまでの頂点のコストの総和を求める
            update_edge(u, v, w)      : uとvをつなぐ辺のコストをwにする
            update_vertex(v, w)       : 頂点vのコストをwにする
            print()                   : オイラーツアー表示
        '''
        self.N = N

        if vertex_cost == False: vertex_cost = [0] * N

        start = 0; time = 0
        EDGE_ORDER = []
        DEPTH_ORDER = []
        VERTEX_COST_ORDER = []
        EDGE_COST_ORDER = []
        now_depth = -1
        
        IN = [-1] * N
        OUT = [-1] * N
        que = [~start, start]
        EDGE_COST = [0] * N
        parents = [-1] * N
        while que:
            v = que.pop()
            now_depth += 1 if v >= 0 else -1
            if v >= 0:
                IN[v] = time
                for nx, edge_cost in node[v][::-1]:
                    if IN[nx] != -1: continue
                    EDGE_COST[nx] = edge_cost
                    que.extend([~nx, nx])
                    parents[nx] = v
                EDGE_ORDER.append(v)
                VERTEX_COST_ORDER.append(vertex_cost[v])
                EDGE_COST_ORDER.append(EDGE_COST[v])
            else:
                OUT[~v] = time
                EDGE_ORDER.append(-~v)
                VERTEX_COST_ORDER.append(-vertex_cost[~v])
                EDGE_COST_ORDER.append(-EDGE_COST[~v])

            DEPTH_ORDER.append(now_depth)
            time += 1

        self.IN = IN
        self.OUT = OUT
        self.EDGE_ORDER = EDGE_ORDER
        self.DEPTH_ORDER = DEPTH_ORDER
        self.VERTEX_COST_ORDER = VERTEX_COST_ORDER
        self.EDGE_COST_ORDER = EDGE_COST_ORDER

        self.edge_bit = BIT(len(EDGE_COST_ORDER))
        for i in range(len(EDGE_COST_ORDER)):
            self.edge_bit.add(i + 1, EDGE_COST_ORDER[i])

        self.vertex_bit = BIT(len(VERTEX_COST_ORDER))
        for i in range(len(VERTEX_COST_ORDER)):
            self.vertex_bit.add(i + 1, VERTEX_COST_ORDER[i])

        self.depth_rmq = RMQ(DEPTH_ORDER)
        self.parents = parents
        self.vertex_cost = vertex_cost

    def lca(self, x, y):
        l = min(self.IN[x], self.IN[y])
        r = max(self.OUT[x], self.OUT[y])
        idx = self.depth_rmq.query(l, r)
        edge = self.EDGE_ORDER[idx]
        if edge < 0:
            lca = self.parents[-edge]
        else:
            lca = edge

        return lca
    
    # 根からxまでの距離
    def root_path_edge_length(self, x):
        # 辺の合計
        return self.edge_bit.sum(self.IN[x] + 1)
    
    # 根からxまでの頂点のコストの総和
    def root_path_vertex_cost(self, x):
        return self.vertex_bit.sum(self.IN[x] + 1)
    
    # uからvまでの距離
    def uv_path_edge_length(self, u, v):
        return self.root_path_edge_length(u) + self.root_path_edge_length(v) - 2 * self.root_path_edge_length(self.lca(u, v))

    # uからvまでの頂点のコストの総和
    def uv_path_vertex_cost(self, u, v):
        v_lca = self.lca(u, v)
        return self.vertex_cost[v_lca] + self.root_path_vertex_cost(u) + self.root_path_vertex_cost(v) - 2 * self.root_path_vertex_cost(v_lca)
    
    # uとwをつなぐ辺のコストをwにする
    def update_edge(self, u, v, w): 
        if self.IN[u] > self.IN[v]: u, v = v, u
        self.edge_bit.update(self.IN[v] + 1, w)
        self.edge_bit.update(self.OUT[v] + 1, -w)
        self.EDGE_COST_ORDER[self.IN[v]] = w
        self.EDGE_COST_ORDER[self.OUT[v]] = -w

    # 頂点vのコストをwにする
    def update_vertex(self, v, w):
        self.vertex_bit.update(self.IN[v] + 1, w)
        self.vertex_bit.update(self.OUT[v] + 1, -w)
        self.VERTEX_COST_ORDER[self.IN[v]] = w
        self.VERTEX_COST_ORDER[self.OUT[v]] = -w

    def print(self):
        '''
            頂点iの根に近い辺をi
                ↓の時 : +i
                ↑の時 : -i
        '''
        print("[NODE]", " ".join(map(lambda x: str(x).rjust(3), range(self.N))))
        print("[ IN ]", " ".join(map(lambda x: str(x).rjust(3), self.IN)))
        print("[ OUT]", " ".join(map(lambda x: str(x).rjust(3), self.OUT)))
        print()
        print("[ TIME]", " ".join(map(lambda x: str(x).rjust(3), range(len(self.EDGE_ORDER)))))
        print("[ EDGE]", " ".join(map(lambda x: str(x).rjust(3), self.EDGE_ORDER)))
        print("[DEPTH]", " ".join(map(lambda x: str(x).rjust(3), self.DEPTH_ORDER)))
        print("[VCOST]", " ".join(map(lambda x: str(x).rjust(3), self.VERTEX_COST_ORDER)))
        print("[ECOST]", " ".join(map(lambda x: str(x).rjust(3), self.EDGE_COST_ORDER)))