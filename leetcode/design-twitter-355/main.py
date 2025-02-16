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
