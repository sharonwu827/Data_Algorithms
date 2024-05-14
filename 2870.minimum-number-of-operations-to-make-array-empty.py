#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dict_ = Counter(nums)
        res = 0
        for val in dict_.values():
            if val%2!=0 and val%3!=0:
                return -1
            elif val%3==0:
                res+=val//3
            elif val%2==0:
                res+=val//2
        return res
        
# @lc code=end

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        queue = deque()
        queue.append((root, 0, 0))
        res = defaultdict(list)
        while queue:
            cur, x, y = queue.popleft()
            res[x].append((cur.val, y))
            if cur.left:
                queue.append((cur.left, x-1, y+1))
            if cur.right:
                queue.append((cur.right, x+1, y+1))
        
        # res[-1] = (9, -1)
        # res[0] = [(3, 0), (15,-2)]
        # sort based on x 
        sorted_keys = sorted(res.keys())
        finalRes = []
        for key in sorted_keys:
            tmp = res[key] # (val, y)
            tmp.sort(key = lambda x:x[-1]) # sort based on y
            arr = []
            for val, y in tmp:
                arr.append(val)
            finalRes.append(arr)
        return finalRes


 
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0 
        p2 = 0 
        while p1 < len(word) and p2<len(abbr):
            if abbr[p2].isdigit(): 
                # have leading zeros or replaces an empty substring
                if abbr[p2] == '0':
                    return False
                else:
                    tmpP2 = p2
                    while tmpP2<len(abbr) and abbr[tmpP2].isdigit():
                            tmpP2+=1
                    length = int(abbr[p2:tmpP2])
                    p1+=length
                    p2 = tmpP2
            else:
                if word[p1] != abbr[p2]:
                    return False
                p1+=1
                p2+=1
        return p1 == len(word) and p2 == len(abbr)

                    
                        
                            


                


