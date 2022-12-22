#!/usr/bin/python

import sys
import os
import random

def start_children():
    child = os.fork()
    if child == 0:
        arg = str(random.randint(10, 15))
        os.execl("./child.py", "child.py", arg)
    print(f"Parent [{os.getpid()}]: children process with PID - {child} ran")


children_number = sys.argv[1]
children_number = int(children_number)

for i in range(0, children_number):
    start_children()

while children_number > 0:
    child_pid, status = os.wait()
    status = status / 256
    status = int(status)
    print(f"Parent[{os.getpid()}]: child process with PID - {child_pid} terminated. Exit Status {status}.")
    if status == 0:
        children_number = children_number - 1
    else:
        start_children()