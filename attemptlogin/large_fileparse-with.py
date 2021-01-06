#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginSuccess = 0 # counter for success
failedIPs = []

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            ip = line.split(" ")[-1].split("\n")[0]
            failedIPs.append(ip)
        elif "-] Authorization failed" in line:
            loginSuccess +=1

print(f"There were {loginfail} failed log in attempts from IP addresses {failedIPs}\nThe number of successful log in attemts was {loginSuccess}")
