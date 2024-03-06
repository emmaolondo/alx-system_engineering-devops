#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    """ return information about an employee """

    if len(sys.argv) != 2:
        sys.exit(1)

    employeeId = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/user/{}/todos'.format(employeeId)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId)

    user = requests.get(user_url).json()
    name = user.get('name')

    taskCount = 0
    t_completed = 0
    list_tasks = []

    todo = requests.get(todo_url)
    tasks = todo.json()

    for i in tasks:
        if i.get('userId') == int(employeeId):
            taskCount += 1
            if i.get('completed'):
                list_tasks.append(i.get('title'))
                t_completed += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, t_completed, taskCount))

    for tasks in list_tasks:
        print('\t', tasks)
