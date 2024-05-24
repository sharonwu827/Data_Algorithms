



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:



class Solution:
    def verticalOrder(self, root):
        # root (0, 0)
        # root.left (-1, 1) root.right (1, 1)
        # sort based on x val, y val
        if not root:
            return 
        queue = deque()
        queue.append((root, 0, 0))
        res = defaultdict(list) # {x:(y, val)}
        while queue:
            cur, x, y = queue.popleft()
            res[x].append([y, cur.val])
            if cur.left:
                queue.append((cur.left, x-1, y+1))
            if cur.right:
                queue.append((cur.right, x+1, y+1))
        
        sortKey = sorted(res.keys()) # 这里不是res.keys().sort()
        finalRes = []
        for key in sortKey:
            values = res[key] # (0,3), (1, 15)
            values.sort(key = lambda x:x[0])
            tmp = []
            for i in range(len(values)):
                tmp.append(values[i][1])
            finalRes.append(tmp)
        return finalRes
    
        
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:   


