#
# @lc app=leetcode id=2365 lang=python3
#
# [2365] Task Scheduler II
#

# @lc code=start
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = 0
        dict_ = defaultdict(int) # (task: nth day) Store the last completed day for each task
        
        for task in tasks:
            # # Check if the task has been completed before and the space requirement is not met
            if task not in dict_ or (days - dict_[task]>=space):
                days+=1
                dict_[task] = days
            # 如果此时iterate到了重复元素
            # check whether the day difference >= space
            # if so, udpate dict_ task 的使用天数
            else:
                days = dict_[task]+space+1
                dict_[task] = days
            
        return days


        
# @lc code=end

