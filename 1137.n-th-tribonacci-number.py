#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0 for _ in range(n + 1)]
        def memoizationSearch(n):
            if n ==0:
                return 0
            if n == 1 or n == 2:
                return 1
            if cache[n]!=0:
                return cache[n]
            for i in range(3, n+1):
                first = memoizationSearch(n-1)
                second = memoizationSearch(n-2)
                third = memoizationSearch(n-3)
            cache[n] = first+second+third
            return first+second+third
        
        return memoizationSearch(n)



    
# @lc code=end

