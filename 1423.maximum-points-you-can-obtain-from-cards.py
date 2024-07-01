#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        max_score = 0
        window_sum = sum(cardPoints[:n-k])  # Initial sum of the first n-k elements
        
        for i in range(k + 1):
            current_sum = window_sum + sum(cardPoints[n-k+i:n])  # Sum of current window
            max_score = max(max_score, current_sum)
            if i < k:
                window_sum += cardPoints[n-k+i] - cardPoints[i]  # Slide the window to the right
        
        return max_score


            
            
  
# @lc code=end

