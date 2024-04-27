#!/usr/bin/python3
"""
Gather data
"""
import csv
import requests
from sys import argv


def main():
    """
    Main function
    """
    if len(sys.argv) == 2:
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            id
        )

        user = requests.get(user_url).json()
        todo_tasks = requests.get(todo_url).json()
        csv2 = csv.writer(open("{}.csv".format(int(argv[1])), "w"), quoting=csv.QUOTE_ALL)
        for task in todos:
            csv2.writerow(
                [user["id"], user["username"], task["completed"], task["title"]]
            )
