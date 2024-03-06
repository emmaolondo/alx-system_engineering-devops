#!/usr/bin/python3
""" Accessing the Reddit API to get number of subscribers """
import requests
import sys

def number_of_subscribers(subreddit):
    """
    Function that accesses the REDDIT API
    If not valid return 0

    Args:
        subreddit (str) : The name of subreddit

    Return:
        int: The number of subscribers, or 0
    """
    url =  "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
