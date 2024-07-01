#
# @lc app=leetcode id=1152 lang=python3
#
# [1152] Analyze User Website Visit Pattern
#

# @lc code=start
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dict_ = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website), key= lambda x: (x[0], x[1])):
            dict_[u].append(w)
        patternCount = defaultdict(int)
        for patterns in dict_.values():
            for i in set(combinations(patterns, 3)):
                patternCount[i] += 1
        for pattern, count in sorted(patternCount.items(), key= lambda x: (-x[1], x[0])):
            return list(pattern)
        

    
        
    
# @lc code=end

