#!/usr/bin/python3
import requests
"""
    a function that queries the Reddit API and
    returns the number of subscribers
"""


def top_ten(subreddit):
    """ return 10 hot posts listed for a given subreddit """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-agent': '0X16API_ADVANCED'}
    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return 0
    result = response.json()
    data = result['data']['children']
    for i in data:
            title = listing.get('data').get('title')
            print(title)

    
