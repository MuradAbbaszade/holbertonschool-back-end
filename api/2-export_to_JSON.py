#!/usr/bin/python3
"""
Gather data
"""
import requests
from sys import argv
import json


if len(argv) == 2:
    url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}/users/{}".format(url, id)
    todo_url = "{}/todos?userId={}".format(
        url, id
    )

    user = requests.get(user_url).json()
    todo_tasks = requests.get(todo_url).json()
    employee_tasks = []
    for task in todo_tasks:
        if task.get("userId") == int(argv[1]):
            employee_tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": task.get("username")
            })
    with open('{}.json'.format(int(argv[1])), mode='w') as file:
        json.dump({int(argv[1]): employee_tasks}, file, indent=4)

