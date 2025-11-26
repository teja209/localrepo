#  make a task tracker that works in cli
'''
how it works: runs the script, it greets in cli, it gives the user options to select from
the options are add, update, delete tasks; and mark the status of a task, and list the tasks
'''
import json
db=[]
with open("userdb.json", 'a') as db1:
    db=db1
t=True
print("hi what do you wanna do today\n")

while t:
    input_=input()
    
    if input_=="add":
        task_name=input()


    elif input_ == "end" or input_ == "\n":
        break
