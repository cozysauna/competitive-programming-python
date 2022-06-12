class RMQ:
    def __init__(self, array):
        N = len(array)
        self.e = 10 ** 18
        self.num = 1 << (N - 1).bit_length()
        self.tree = [self.e] * 2 * self.num
        self.index = [None] * 2 * self.num 
        for i in range(N):
            self.tree[self.num + i] = array[i]
            self.index[self.num + i] = i 

        for i in range(self.num - 1, 0, -1):
            if self.tree[2 * i] <= self.tree[2 * i + 1]:
                self.tree[i] = self.tree[2 * i]
                self.index[i] = self.index[2 * i]
            else:
                self.tree[i] = self.tree[2 * i + 1]
                self.index[i] = self.index[2 * i + 1]

    def query(self, l, r): #(mn, idx)
        l += self.num
        r += self.num
        mn, idx = self.e, None

        while l < r:
            if l & 1:
                if mn >= self.tree[l]:
                    mn = self.tree[l]
                    idx = self.index[l]
                l += 1
            if r & 1:
                if mn >= self.tree[r - 1]:
                    mn = self.tree[r - 1]
                    idx = self.index[r - 1]

            l >>= 1
            r >>= 1
        return mn, idx 

class RSQ:
    def __init__(self, array):
        N = len(array)
        self.e = 0
        self.num = 1 << (N - 1).bit_length()
        self.tree = [self.e] * 2 * self.num
        for i in range(N): self.tree[self.num + i] = array[i]
        for i in range(self.num - 1, 0, -1): self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, l, r): # [l, r)
        ret = self.e
        l += self.num
        r += self.num
        while l < r:
            if l & 1: ret += self.tree[l]; l += 1
            if r & 1: ret += self.tree[r - 1]
            l >>= 1
            r >>= 1
        return ret

class EulerTour:
    def __init__(self, N, node, start = 0):
        self.N = N 
        self.node = node 
        self.info_index = [
            {
                'depth':None, 
                'in': None, 
                'out': None
            } 
            for _ in range(N)
        ]
        self.step = 0
        self._dfs_index(start)
        self.info_step = [
            {
                'now': None, 
                'in_v_cost': None, 
                'in_e_cost': None, 
                'depth': None
            }
            for _ in range(self.step)
        ]
        self._initialize_step()
        self._dfs_step(start)

        # LCA
        depths = [self.info_step[i]['depth'] for i in range(self.step)]
        self.depth_rmq = RMQ(depths)

        #subtree_nodes_cost
        nodes = []
        for i in range(self.step):
            _in_v_cost = self.info_step[i]['in_v_cost']
            if _in_v_cost == None: _in_v_cost = 0
            nodes.append(_in_v_cost)
        self.nodes_rsq = RSQ(nodes)

        #subtree_edges_cost 
        edges = []
        for i in range(self.step):
            _in_e_cost = self.info_step[i]['in_e_cost']
            if _in_e_cost == None: _in_e_cost = 0
            edges.append(_in_e_cost)
        self.edges_rsq = RSQ(edges)

    def get_lca(self, x, y):
        L = min(self.info_index[x]['in'], self.info_index[y]['in'])
        R = max(self.info_index[x]['out'], self.info_index[y]['out'])
        idx = self.depth_rmq.query(L, R)[1]
        return self.info_step[idx]['now']

    def get_subtree_nodes_cost(self, x):
        L = self.info_index[x]['in']
        R = self.info_index[x]['out']
        return self.nodes_rsq.query(L, R - 1)

    def get_subtree_edges_cost(self, x):
        L = self.info_index[x]['in']
        R = self.info_index[x]['out']
        return self.edges_rsq.query(L + 1, R - 1)

    def _initialize_step(self): self.step = 0
    def _add_step(self): self.step += 1

    def _dfs_index(self, x, p = -1, depth = 0):
        self.info_index[x]['depth'] = depth
        self.info_index[x]['in'] = self.step
        self._add_step()
        for nx, _ in self.node[x]:
            if nx == p: continue
            self._dfs_index(nx, x, depth + 1)
            self._add_step()
        
        self.info_index[x]['out'] = self.step

    def _dfs_step(self, x, p = -1, depth = 0, cost = 0):
        self.info_step[self.step] = {
            'now': x, 
            'in_v_cost': x, 
            'in_e_cost': cost, 
            'depth': depth
        }
        self._add_step()
        for nx, c in self.node[x]:
            if nx == p: continue
            self._dfs_step(nx, x, depth + 1, c)
            self.info_step[self.step] = {
                'now': x, 
                'in_v_cost': None, 
                'in_e_cost': None, 
                'depth': depth
            }
            self._add_step()

    def verbose(self):
        print('INDEX', *self.info_index, sep = '\n')
        print('STEP', *self.info_step, sep = '\n')