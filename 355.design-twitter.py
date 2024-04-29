#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
class Twitter:
    def __init__(self):
        # user:[followers]
        self.follower = defaultdict()
        # user:[tweetIds]
        self.tweet = defaultdict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        heap = []
        heapq.heappush(heap, -tweetId)
        self.tweet[userId] = heap
        
    def getNewsFeed(self, userId: int) -> List[int]:
        # Retrieves the 10 most recent tweet IDs
        minLen = min(self.tweet[userId], 10)
        res = []
        for _ in range(minLen):
            tmp = -heapq.heappop(self.tweet[userId])
            res.append(tmp)
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].append(followeeId)
        for tweetId in self.tweet[followeeId]:
            heapq.heappush(self.tweet[followerId], -tweetId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].remove(followeeId)
        self.tweet[followerId].remove(self.tweet[followeeId])
    

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

