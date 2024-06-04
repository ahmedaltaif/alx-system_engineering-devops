#!/usr/bin/python3
""" a function that queries the Reddit API and returns the number"""
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "0X16API_ADVANCED)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
