__author__ = 'ambli'

MAX_LENGTH = 10

def split_into_minitweets(s):
    """ (str) -> list of str

    Precondition: len(s) >= 1

    Return a list containing the mini-tweets in s. Maximize the length of each
    mini-tweet, so that each mini-tweet (except possibly the last) has a length
    equal to MAX_LENGTH.

    >>> s = 'code.org'
    >>> split_into_minitweets(s)
    ['code.org']
    >>> s = 'Do not just play on your phone - program it. - @BarackObama'
    >>> split_into_minitweets(s)
    ['Do not jus', 't play on ', 'your phone', ' - program', ' it. - @Ba', 'rackObama']
    """
    miniTweet_List = []
    mini_tweet = ""
    tweet_length = 0
    i = 0

    while i < len(s):
        if (tweet_length < MAX_LENGTH):
            mini_tweet += s[i]
            tweet_length += 1
        else:
            miniTweet_List.append(mini_tweet)
            mini_tweet = s[i]
            tweet_length = 1

        i += 1

    miniTweet_List.append(mini_tweet)

    return miniTweet_List

# Test
s = 'code.org'
miniTweetList = split_into_minitweets(s)
print miniTweetList

s = 'Do not just play on your phone - program it. - @BarackObama'
miniTweetList = split_into_minitweets(s)
print miniTweetList


