#!/usr/bin/python3
"""
Gather data
"""
import requests
from sys import argv
import json


if len(argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}/users/{}".format(url, int(argv[1]))
    todo_url = "{}/todos?userId={}".format(
        url, int(argv[1])
    )

    user = requests.get(user_url).json()
    todo_tasks = requests.get(todo_url).json()
    employee_tasks = {f"{int(argv[1])}": []}
    for task in todo_tasks:
        t = {}
        t["task"] = task["title"]
        t["completed"] = task["completed"]
        t["username"] = user["username"]
        employee_task[f"{int(argv[1])}"].append(t)

    with open('{}.json'.format(int(argv[1])), mode='w') as file:
        json.dump({int(argv[1]): employee_tasks}, file, indent=4)
