#!/usr/bin/python

import sys
import os
import time
import random

proc_id = os.getpid()
parent_proc_id = os.getppid()
sleep_time = sys.argv[1]
sleep_time = int(sleep_time)

print(f"Child [{proc_id}]: Started. PID - {proc_id}, PPID - {parent_proc_id}")

time.sleep(sleep_time)

print(f"Child [{proc_id}]: Ended. PID - {proc_id}, PPID - {parent_proc_id}")

status = random.randint(0, 1)

sys.exit(status)