class Twitter:

    """
    postTweet will append the tweet into tweets list
    follow will add 
    """
    def __init__(self):
        self._followings = {}
        self._feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        count = 0
        # Iterate over the feed in reverse (most recent first)
        for uid, tid in reversed(self._feed):
            if uid == userId or (userId in self._followings and uid in self._followings[userId]):
                res.append(tid)
                count += 1
            if count == 10:
                break  # Stop once we have 10 tweets
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if self._followings.get(followerId):
            self._followings[followerId].add(followeeId)
        else:
            self._followings[followerId] = {followeeId}

        print(self._followings)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self._followings and followeeId in self._followings[followerId]:
            self._followings[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



# New solutions to use heaps.
# The previous solution did not use the heap.

class Twitter2:

    """
    postTweet will append the tweet into tweets list
    follow will add 
    """
    def __init__(self):
        self.followings = dict()
        self.tweets_per_user = dict()
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        if userId not in self.tweets_per_user:
            self.tweets_per_user[userId] = [(self.time, tweetId)]
        else:
            self.tweets_per_user[userId].append((self.time, tweetId))
        
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        
        # if userId not in self.tweets_per_user:
        #     self.tweets_per_user[userId] = []

        if userId in self.followings:
            self.followings[userId].add(userId)
        else:
            self.followings[userId] = set({userId})

        for followee_id in self.followings.get(userId, {}):
            if followee_id in self.tweets_per_user:
                # heap.extend(self.tweets_per_user[followee_id])
                index = len(self.tweets_per_user[followee_id]) - 1
                time, tweet = self.tweets_per_user[followee_id][index]
                heap.append((time, tweet, followee_id, index - 1))

        heapq.heapify(heap)

        while heap and len(feed) < 10:
            _, tweet, followee_id, index = heapq.heappop(heap)
            feed.append(tweet)

            if index >= 0:
                time, new_tweet = self.tweets_per_user[followee_id][index]
                heapq.heappush(heap, (time, new_tweet, followee_id, index - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return

        if self.followings.get(followerId):
            self.followings[followerId].add(followeeId)
        else:
            self.followings[followerId] = set({followeeId})

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return

        if self.followings.get(followerId):
            self.followings[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
