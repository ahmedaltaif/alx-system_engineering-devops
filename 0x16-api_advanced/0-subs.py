#!/usr/bin/python3
"""
    a function that queries the Reddit API and
    returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ return the numer of subscribers """
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    try:
        response = requests.get(url,
                                headers={'User-agent': 'your bot 0.1'},
                                allow_redirects=False).json()
        return response['data'].get('subscribers')
    except Exception:
        return 0
