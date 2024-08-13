#!/usr/bin/python3

'''
A python script that uses a REST API of a given employee ID,
to return information about his/her TODO list progress
'''
import request
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

    print("Employee {} is done with tasks ({}/{}):".format(userName, taskDone, len(todos)))

    for i in tasks:
        title = i.get("title")
        print(title)
