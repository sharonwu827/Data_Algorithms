#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1]*(i+1)
            for j in range(i+1):
                if j == 0:
                    tmp[j] = res[-1][0]
                elif j == i:
                    tmp[j] = res[-1][j-1]
                else:
                    tmp[j] = res[-1][j-1]+res[-1][j]
            res.append(tmp)
        return res


                
                
        
# @lc code=end

