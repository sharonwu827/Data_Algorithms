#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parent = {}
        def add(val):
            if val not in self.parent:
                self.parent[val] = val
        def find(val):
            if val!=self.parent[val]:
                self.parent[val] = find(self.parent[val])
            return self.parent[val]
        def union(val1, val2):
            root1 = find(val1)
            root2 = find(val2)
            if root1!=root2:
                self.parent[root1] = root2
        res = []
        for account in accounts:
            name, master = account[0], account[1]
            add((name, master))
            account = list(set(account[2:]))
            for i in range(len(account)):
                add((name, account[i]))
                union((name,master),(name,account[i]))



            


        
# @lc code=end

