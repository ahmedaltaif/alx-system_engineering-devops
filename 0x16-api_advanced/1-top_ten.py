#!/usr/bin/python3
"""
    a function that queries the Reddit API and
    returns the number of subscribers
"""
import requests


def top_ten(subreddit):
    """ Function that prints the titles """

    base_url = 'https://www.reddit.com'
    sort = 'top'
    limit = 10
    url = '{}/r/{}/.json?sort={}&limit={}'.format(
        base_url, subreddit, sort, limit)
    headers = {
        'User-Agent':
        '0X16API_ADVANCED'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        if not posts:
            print('None')
        else:
            for post in posts:
                print(post['data']['title'])
    
    except requests.exceptions.RequestException:
        # Handle HTTP errors
        print('None')
    except ValueError:
        # Handle JSON decode error
        print('None')
    except KeyError:
        # Handle missing keys in the response
        print('None')