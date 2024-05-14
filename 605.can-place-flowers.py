#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        temp=[0]+flowerbed+[0]
        for i in range(1,len(temp)-1):
            if temp[i]==temp[i-1]==temp[i+1]==0:
                temp[i]=1
                n-=1
        return n<=0
                    

        
# @lc code=end

