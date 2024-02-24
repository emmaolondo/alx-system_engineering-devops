#!/usr/bin/python3
""" 
Python script that, using this REST API, for a given employee ID,\
        returns information about his/her TODO list progress
"""


import json
import requests
import sys

if __name__ == "__main__":

    # employeeId = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users"

    all_users = requests.get(user_url)
    users = all_users.json()

    employeesData = {}

    todo = requests.get(todo_url)
    tasks = todo.json()
    taskid = tasks.get('userId')

    for u in users:
        # employeeId = u['id']
        # username = u['username']
        employee_tasks = []

        for i in tasks:
            if taskid == u.get('id'):
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
