#!/usr/bin/python3
""" 
Python script that, using this REST API, for a given employee ID,\
        returns information about his/her TODO list progress
"""


import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(1)

    employeeId = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeId}"

    user = requests.get(user_url)
    name = user.json().get('name')

    taskCount = 0
    completed = 0

    todo = requests.get(todo_url)
    tasks = todo.json()

    for i in tasks:
        if i.get('userId') == employeeId:
            taskCount += 1
            if i.get('completed'):
                completed += 1

    print(f"Employee {name} is done with tasks({completed}/{taskCount}):")

    for j in tasks:
        if j.get('userId') == employeeId and j.get('completed'):
            print(f"\n\t{j['title']}", end="")
