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
    if len(argv) == 2:
        url = "https://jsonplaceholder.typicode.com/"
        user_url = "{}/users/{}".format(url, id)
        todo_url = "{}/todos?userId={}".format(
            url, id
        )

        user = requests.get(user_url).json()
        todo_tasks = requests.get(todo_url).json()
        csv2 = csv.writer(
            open("{}.csv".format(int(argv[1])), "w"),
            quoting=csv.QUOTE_ALL
        )
        for task in todo_tasks:
            csv2.writerow(
                [user["id"],
                 user["username"],
                 task["completed"],
                 task["title"]]
            )
