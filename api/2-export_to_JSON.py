#!/usr/bin/python3
"""Gather data"""
import json
import requests
from sys import argv

if len(argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    result = {f"{argv[1]}": []}
    todos = requests.get(f"{url}users/{argv[1]}/todos").json()
    user = requests.get(f"{url}users/{argv[1]}").json()
    for todo in todos:
        t = {}
        t["task"] = todo["title"]
        t["completed"] = todo["completed"]
        t["username"] = user["username"]
        result[f"{argv[1]}"].append(t)

    with open(f"{argv[1]}.json", "w") as f:
        f.write(json.dumps(result))
