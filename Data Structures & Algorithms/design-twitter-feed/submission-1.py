class Twitter:

    def __init__(self):
        self.timer = 0
        self.follower_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.timer, tweetId])

        if(len(self.tweet_map[userId])) > 10:
            self.tweet_map[userId].pop(0)
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed_users = self.follower_map[userId] | {userId}

        candidate_heap = []

        for author_id in feed_users:
            if author_id not in self.tweet_map:
                continue
            
            user_tweets = self.tweet_map[author_id]
            index = len(user_tweets) - 1
            timer, tweetId = user_tweets[index]

            heapq.heappush(candidate_heap, [timer, tweetId, author_id, index - 1])
            
            if(len(candidate_heap)) > 10:
                heapq.heappop(candidate_heap)
            
        feed_heap = []
        while candidate_heap:
            timer, tweetId, author_id, index = heapq.heappop(candidate_heap)
            heapq.heappush(feed_heap, [-timer, tweetId, author_id, index])
        
        tweets = []
        while feed_heap and len(tweets) < 10:
            timer, tweetId, author_id, next_index = heapq.heappop(feed_heap)
            tweets.append(tweetId)

            if next_index >= 0:
                next_timer, next_tweet_id = self.tweet_map[author_id][next_index]
                heapq.heappush(feed_heap, [-next_timer, next_tweet_id, author_id, next_index - 1])

        return tweets
            

            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follower_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].discard(followeeId)
