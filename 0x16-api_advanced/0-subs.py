#!/bin/python3

"""script to retrieve the number of subscribers on subreddit"""

import requests

def number_of_subscribers(subreddit):
     """returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()

    if response.status_code == 200:
        data = response.json()
        no_subs = data.get("data").get("subscribers")
        retuns no_subs
    else:
        return 0
