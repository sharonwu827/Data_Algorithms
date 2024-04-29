#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
class Solution:
    def __init__(self):
        self.parent = {}
        self.num_of_sets = 0

    def add(self, val):
        if val not in self.parent:
            self.parent[val] = val ## parent[x] = x 表示 x 的 parent 是 x
            self.num_of_sets += 1

    def find(self, val):
        if val != self.parent[val]:  # 路径压缩 在查询的过程中，把沿途的每个节点的父节点都设为根节点
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def union(self, x, y):
        '''
        make x's father equal to y's father
        '''
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:  # 其实这里究竟把谁当做父节点一般是没有区别的
            self.parent[root_x] = root_y
            self.num_of_sets -= 1
          
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        for i in range(n):
            self.add(i)

        for connection in connections:
            # self.add(connection[0]) 这样写是错的
            # self.add(connection[1]) 这样写是错的
            self.union(connection[0], connection[1])
        
        # 当计算机的数量为 n 时，我们至少需要 n-1根线才能将它们进行连接
        # 如果线的数量少于 n-1，那么我们无论如何都无法将这 n 台计算机进行连接
        required_connection = self.num_of_sets-1
        available_connections = len(connections)
        if available_connections < n - 1:
            return -1
        else:
            return required_connection
        
# @lc code=end

