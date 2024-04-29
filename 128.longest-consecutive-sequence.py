#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int) # 用于判断某个数是否存在哈希表中
        max_len = 0
        for num in nums:
            if num not in hashmap:
                # 获取当前数的最左/右边连续长度,没有的话就更新为0
                left = hashmap.get(num-1, 0)
                right = hashmap.get(num+1, 0)
                cur_len = left + right + 1
                max_len = max(max_len, cur_len)
                # 更新最左端点的值，如果left=n存在，那么证明当前数的前n个都存在哈希表中
                # For example, if num = 5, left = 2, right = 3
                # then hashmap[5-2] and hashmap[5+3] will be updated to store the length of the sequence starting from 3 and ending at 8.
                hashmap[num-left] = cur_len
                hashmap[num+right] = cur_len
                hashmap[num] = cur_len
        return max_len

                



        
# @lc code=end

