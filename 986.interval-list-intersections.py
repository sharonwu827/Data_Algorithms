#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0 
        p2 = 0 
        res = []
        while p1<len(firstList) and p2<len(secondList):
            if firstList[p1][1]<secondList[p2][0]:
                p1+=1
            elif firstList[p1][0]>secondList[p2][1]:
                p2+=1
            else: 
                left = max(firstList[p1][0], secondList[p2][0])
                right = min(firstList[p1][1], secondList[p2][1])
                res.append([left, right])
                 # Move to the next interval which has the smallest endpoint
                if firstList[p1][1]< secondList[p2][1]:
                    p1+=1
                else:
                    p2+=1
        return res
                



        
# @lc code=end

