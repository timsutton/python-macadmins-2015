#!/usr/bin/python

# Rudimentary usage script. Since 'ac' will require sudo/root to
# get the login time for all users, you should run this script
# with sudo.

import subprocess

usage = {}
p = subprocess.Popen(['ac', '-p'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
lines = out.splitlines()

# take a copy of the existing lines that omits the last line (-1 wraps from the end)
lines = lines[0:-1]
for l in lines:
    user, total = l.split()
    total_f = float(total)
    if user not in usage:
        usage[user] = 0.0
    usage[user] += total_f
for user in usage:
    usage[user] = int(usage[user])
print usage
