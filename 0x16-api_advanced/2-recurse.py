#!/usr/bin/python3
"""
recursive function
"""
import requests


s = requests.Session()
s.headers.update({'User-Agent': '0X16API_ADVANCED'})
s.allow_redirects = False


def recurse(subreddit, hot_list=[]):
    """recursively grab subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = s.get(url).json()
    try:
        for tit in response['data']['children']:
            hot_list.append(tit['data']['title'])
        if response['data']['after']:
            s.params = {'after': response['data']['after']}
            return recurse(subreddit, hot_list)
        return hot_list
    except Exception:
        return None
