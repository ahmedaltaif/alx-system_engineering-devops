#!/usr/bin/python3
"""
    a function that queries the Reddit API and
    returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ return the numer of subscribers """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': '0X16API_ADVANCED'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
