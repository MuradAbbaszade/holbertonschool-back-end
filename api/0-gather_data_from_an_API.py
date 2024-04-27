#!/usr/bin/python3
"""
Gather data
"""
import requests
from sys import argv


def main(id):
    """
    Main function
    """
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        id
    )

    user = requests.get(user_url).json()
    todo_tasks = requests.get(todo_url).json()
    username = user.get("name")
    task_length = len(todo_tasks)
    completed_tasks = []
    for task in todo_tasks:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))
    completed_tasks_length = len(completed_tasks)
    print(
        "Employee {} is done with tasks({}/{}):".format(
            username, completed_tasks_length, task_length
        )
    )

    for task in completed_tasks:
        print("\t " + task)


if __name__ == "__main__":
    if len(argv) == 2:
        id = int(argv[1])
        main(id)
