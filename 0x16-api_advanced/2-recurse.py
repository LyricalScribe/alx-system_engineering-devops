#!/usr/bin/python3

    """ script to recursively call an api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ function to recursively call an api"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(subreddit, after)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if posts.status_code == 200:
        posts = response.json()['data']['chilren']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = response.json()['data']['after']
        if after is not None:
            recurse(subreddit, hot_list=hot_list, after=after)
        return hot_list
    else:
        return None

