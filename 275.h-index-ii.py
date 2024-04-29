#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=startfrom typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # verify whether at least h papers have at least h citations
        def paperPublished(h):
            count = 0
            for citation in citations:
                if citation >= h:
                    count += 1
            return count >= h

        left = 0
        right = max(citations) + 1

        while left < right:
            mid = left + (right - left) // 2
            if paperPublished(mid):
                left = mid + 1
            else:
                right = mid

        return left -1 

        
# @lc code=end

