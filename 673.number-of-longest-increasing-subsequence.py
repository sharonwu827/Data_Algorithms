#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]: the longest subsequences at nums[i]
        dp = [1]*n
         # dp[i]: number of subsequence that have the longest subsequences at nums[i]
        cnt = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[i]>dp[j]+1:
                        cnt[i] = cnt[j]
                    elif dp[i]==dp[j]+1:
                        cnt[i] += cnt[j]
        maxFreq = 0 
        maxLen = 0 
        for i in range(n):
            if dp[i]>maxLen:
                maxLen = dp[i]
                maxFreq = cnt[i]
        return maxFreq


        
# @lc code=end



class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        queue = deque()
        queue.append((root, 0, 0))
        cache = defaultdict(list)
        while queue:
            cur, x, y = queue.popleft()
            cache[x].append((cur.val, y))
            if cur.left:
                queue.append((cur.left, x-1, y+1))
            if cur.right:
                queue.append((cur.right, x+1, y+1))
            
        res = []
        #  defaultdict doesn't have a method sort, 
        sorted_keys = sorted(cache.keys())
        for x in sorted_keys:
            cache[x].sort(key=lambda x:x[-1])
            tmp = []
            for val, y in  cache[x]:
                tmp.append(val)
            res.append(tmp)
        return res
        
        
        
