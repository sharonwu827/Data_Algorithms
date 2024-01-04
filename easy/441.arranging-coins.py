#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        def coinNeed(row):
            # for building rows, how many coins are needed
            # using the formula for the sum of the first k natural numbers
            return (row * (row + 1)) // 2
        
        left = 1
        right = n # int(math.sqrt(2*n))
        while left<right:
            mid = left+(right-left)//2
            # minimize size of row that make the coin neede >n
            if coinNeed(mid)==n:
                return mid
            elif coinNeed(mid)>n:
                right = mid
            else:
                left = mid+1
        return left-1
          
# @lc code=end

