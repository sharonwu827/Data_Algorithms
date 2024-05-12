#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        self.arr.append(value)
        
    def getIntervals(self) -> List[List[int]]:

        
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        