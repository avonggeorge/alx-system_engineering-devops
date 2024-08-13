#!/usr/bin/python3
'''
Script that uses employee ID of a
REST API return info about todo list progress
'''

import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    mainUrl = "https://jsonplaceholder.typicode.com/users/"
    url = mainUrl + userId
    getUrl = requests.get(url)
    userName = getUrl.json().get("name")

    todoUrl = url + "/todos"
    getTodoUrl = requests.get(todoUrl)
    todos = getTodoUrl.json()

    taskDone = 0
    tasks = []

    for i in todos:
        if i.get("completed"):
            tasks.append(i)
            taskDone += 1

    print("Employee {} is done with tasks({}/{}):"
            .format(userName, taskDone, len(todos)))

    for i in tasks:
        title = i.get("title")
        print("\t {}".format(title))