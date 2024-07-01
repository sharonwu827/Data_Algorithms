#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()  # 双端队列
        n = len(nums)
        res = []
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            # 目前队列已满。
            # 但是新元素需要进来，所以列表最左侧的下标出队列
            if i-stack[0] >=k:
                stack.popleft()
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                res.append(nums[stack[0]])
        return res

               
        
# @lc code=end

