#!/usr/bin/python3
"""
    a function that queries the Reddit API and
    returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    """ return 10 hot posts listed for a given subreddit """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': '0X16API_ADVANCED'}
    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False).json()
        data = response['data']['children']
        for listing in data:
            title = listing.get('data').get('title')
            print(title)
    except Exception:
        print('None')
