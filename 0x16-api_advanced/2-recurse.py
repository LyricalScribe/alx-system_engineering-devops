#!/usr/bin/python3
""" script to recursively call an api"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """return list of all hot posts titles of a subreddit """

    headers = {'User-agent': 'my agent'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
            subreddit, after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        after = data['after']
        articles = data['children']
        for article in articles:
            hot_list.append(article['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return (hot_list)
    else:
        return (None)
