#
# @lc app=leetcode id=2781 lang=python3
#
# [2781] Length of the Longest Valid Substring
#

# @lc code=start

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)
        left = 0   # 窗口左端点
        res = 0 # 最终结果
        for right in range(len(word)):
            for i in range(right, max(right - 10, left - 1), -1):
                if word[i: right + 1] in forbiddenSet: 
                    left = i + 1
                    break
            res = max(res, right - left + 1)
        return res



class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        # minInd = nums.index(min(nums))
        # maxInd = nums[::-1].index(max(nums))
        minInd = 0
        maxInd = 0 
        moveMax = 0
        moveMin = 0 
        for i in range(1, n):
            if nums[i]>=nums[maxInd]:
                maxInd = i
            if nums[i]<nums[minInd]:
                minInd = i
        if minInd > maxInd:
            # mean if we moove maxInd, the minind will change
            moveMax = n-1-maxInd
            moveMin = minInd-1

        else:
            moveMin = minInd
            moveMax = n-1-maxInd
            
        return moveMin+moveMax
            
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        arr = [] * n
        for i in range(n):
            arr[i] = [timestamp[i],username[i], website[i]]
        # Sort based on time
        arr.sort(key = lambda x:x[0])
        # form a dictionary; users as key and website list as value
        user_and_web = defaultdict() # user:website
        for i in range(n):
            user_and_web[username[i]].append(website[i])
        
        # form another dict where 3-sequence of websites as key and their counts as value
        web_and_cnt = defaultdict()
        for key in user_and_web.keys:
            if len(user_and_web[key])>=3:
                allPath = self.getCombination(user_and_web[key])
                for path in allPath:
                    web_and_cnt[path].append(key)
        
        max_score = max(web_and_cnt.values())
        max_patterns = [pattern for pattern, score in web_and_cnt.items() if score == max_score]
        max_patterns.sort()  # Sort lexicographically

        return max_patterns[0]
        
        def getCombinatio n(arr):
            res= []
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    for k in range(j+1, len(arr)):
                        res.append(arr[i], arr[j], arr[k])





class Solution:
    def minimumKeypresses(self, s: str) -> int:
        dict_ = Counter(s)
        for i in range(len(dict_))
        
                    

        