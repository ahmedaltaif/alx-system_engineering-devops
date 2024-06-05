#!/usr/bin/python3
"""
recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Function recurse """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': '0X16API_ADVANCED'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        for post in response.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if response.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
