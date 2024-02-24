#!/usr/bin/python3
""" 
Python script that, using this REST API, for a given employee ID,\
        returns information about his/her TODO list progress
"""


import csv
import requests
import sys

if __name__ == "__main__":

    # check arguments passed
    if len(sys.argv) != 2:
        sys.exit(1)

    employeeId = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employeeId}"

    user = requests.get(user_url)
    name = user.json().get('name')

    taskCount = 0
    completed = 0
    csv_data = []
    completed_status = False

    todo = requests.get(todo_url)
    tasks = todo.json()

    # check progress and prepare csv data file
    for i in tasks:
        # csv_data = []
        if i.get('userId') == employeeId:
            taskCount += 1
            if i.get('completed'):
                completed += 1
                completed_status = True
            csv_row = [employeeId, name, i['completed'], i['title']]
            csv_data.append(csv_row)

    # print user progress
    print(f"Employee {name} is done with tasks({completed}/{taskCount}):")

    # get tasks completed
    for j in tasks:
        if j.get('userId') == employeeId and j.get('completed'):
            print(f"\n\t{j['title']}", end="")


    # export data to csv format
    filename = f"{employeeId}.csv"

    # open file in write mode
    with open(filename, 'w', newline='') as file:
        # create a csv writer file
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        # write data to the csv file
        # writer.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])

        # write multiple rows at once
        writer.writerows(csv_data)
