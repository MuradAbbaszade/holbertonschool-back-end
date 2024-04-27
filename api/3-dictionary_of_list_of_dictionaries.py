#!/usr/bin/python3
"""Gather data"""
import json
import requests


url = "https://jsonplaceholder.typicode.com/"
users = requests.get(f"{url}users").json()
all_tasks = {}
for u in users:
    id = u["id"]
    username = u["username"]
    user = requests.get(f"{url}users/{id}/todos").json()
    all_tasks[f"{id}"] = []
    for i in user:
        todos = {}
        todos["username"] = username
        todos["task"] = i["title"]
        todos["completed"] = i["completed"]
        all_tasks[f"{id}"].append(todos)

with open("todo_all_employees.json", "w") as f:
    f.write(json.dumps(all_tasks))
