#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str):
        # 统计该字符串中需要最少删除多少个左右括号才能保证有效
        def getMinRemove(s):
            leftToRemove = 0 
            rightToRemove = 0 
            for i, char in enumerate(s):
                if char == '(':
                    leftToRemove+=1
                if char == ')':
                    if not leftToRemove:
                        rightToRemove+=1
                    else:
                        leftToRemove-=1
            # 最少需要去掉的左括号的数目和右括号的数目 
            return [leftToRemove, rightToRemove]
        # 2. 判断字符串是否合法有效。
        def isValid(self, s: str) -> bool:
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        res = []
        def backtracking(startInd, leftToRemove, rightToRemove, path):
            nonlocal res
            if not leftToRemove and not rightToRemove and isValid(path):
                res.add(''.join(path.copy()))
                return 
            
            for i in (startInd, len(path)):
                # 去重复
                if i > startInd and path[i] == path[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if leftToRemove + rightToRemove > len(path) - i:
                    return
                if leftToRemove>0 and path[i] == '(':
                    backtracking(i, leftToRemove-1, rightToRemove, path[:i] + path[i + 1:])
                if rightToRemove>0 and path[i] == ')':
                    backtracking(i, leftToRemove, rightToRemove-1, path[:i] + path[i + 1:])

        
        leftToRemove, rightToRemove = getMinRemove(s)
        backtracking(0, leftToRemove, rightToRemove, s)
        return res
    

    



        
# @lc code=end

