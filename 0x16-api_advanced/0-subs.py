#!/usr/bin/python3
import requests


""" a function that queries the Reddit API and returns the number of subscribers """
def number_of_subscribers(subreddit):
    """ return the numer of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-agent' : '0X16API_ADVANCED'},
                                                 allow_redirects=False).json()
    if response.status_code != 200:
        return 0
    result = response.get("data")
    return result.get("subscribers")
