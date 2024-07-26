#!/usr/bin/python3
""" 
Python script that, using this REST API, for a given employee ID,\
        returns information about his/her TODO list progress
"""


import json
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(1)

    # employeeId = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users"

    all_users = requests.get(user_url)
    users = all_users.json()

    taskCount = 0
    completed = 0
    employeesData = {}

    todo = requests.get(todo_url)
    tasks = todo.json()

    for u in users:
        # employeeId = u['id']
        # username = u['username']
        employee_tasks = []

        for i in tasks:
            if i['userId'] == u.get('id'):
                taskCount += 1
                if i.get('completed'):
                    completed += 1
                tasks = {"username": u.get('username'), "task": i['title'], "completed": i['completed']}
            employee_tasks.append(tasks)
        employeesData[u.get('id')] = employee_tasks

    print(f"Employee {name} is done with tasks({completed}/{taskCount}):")

    """
    for j in tasks:
        if j.get('userId') == employeeId and j.get('completed'):
            print(f"\n\t{j['title']}", end="")
    """

    with open('todo_all_employees.json', 'w') as file:
        json.dump(employeesData, file, indent=2)
