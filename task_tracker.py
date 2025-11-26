#  make a task tracker that works in cli
'''
how it works: runs the script, it greets in cli, it gives the user options to select from
the options are add, update, delete tasks; and mark the status of a task, and list the tasks
'''
import json
import time
db={}
t=True
with open("userdb.json", 'a') as db1:
    db=db1

while t:
    input_=input("enter what you wanna do")
    if input_.startswith("add"):
        task=input_[4:]
        db
    elif input_.startswith("update"):
        ...
    elif input_.startswith("delete"):
        ...
    elif input_.startswith("list"):
        ...
    elif input_.startswith("list of done"):
        ...
    elif input_.startswith("list of todo"):
        ...
    elif input_.startswith("list of ongoing"):
        ...
    elif input_=="\n":
        t=False
    else:
        print("invalid function enter proper function")