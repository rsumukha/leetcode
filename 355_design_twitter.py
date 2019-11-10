"""
PT - Merge k sorted arrays concept
"""
import collections

class Twitter(object):

    def __init__(self):
        self.followdict = collections.defaultdict(set)
        self.map = collections.defaultdict(collections.deque)
        self.time = 1
        

    def postTweet(self, userId, tweetId):
        self.follow(userId, userId)
        self.map[userId].appendleft([self.time, tweetId])
        self.time +=1 
        

    def getNewsFeed(self, userId):
        result = []
        heap = []
        followers = self.followdict[userId]
        fset = set()
        
        for follower in followers:
            if len(self.map[follower])!=0:
                heapq.heappush(heap, (-1*self.map[follower][0][0], self.map[follower][0][1], 0, follower ) )
                fset.add(follower)  
        
        while len(heap)!=0 and len(result)<10 and fset:
            m, tweet, idx, f = heapq.heappop(heap)
            result.append(tweet)
            if idx == len(self.map[f])-1:
                fset.remove(f)
            else:
                idx+=1
                heapq.heappush(heap, (-1*self.map[f][idx][0], self.map[f][idx][1], idx, f))
        return result
            

    def follow(self, followerId, followeeId):
        self.followdict[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followdict[followerId] and followerId != followeeId:
            self.followdict[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
