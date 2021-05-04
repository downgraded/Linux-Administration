import re
import json
import subprocess

activity = []

os = subprocess.check_output(['cat', '/etc/os-release'])    # determine host os, to select appropriate ssh logfile
if b'CentOS' in os:
    logfile = '/var/log/secure'
elif b'Ubuntu' in os:
    logfile = '/var/log/auth.log'

def extractIPs():                                           # Locate IP addresses in /var/log/secure file
    ipAddresses = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b' # and return list for further processing

    with open(logfile, 'r') as f:
        ipList = re.findall(ipAddresses, f.read())
        ipList = list(set(ipList)) # remove duplicate entries
        f.close()
    return ipList

def findActivity(IP):
    activity = {}
    failedUsers = {}
    failedUsersList = []
    successfulLogins = {}

    with open(logfile, 'r') as f:
        for i in f.readlines():
            i = re.sub("\s\s+", " ", i) # Convert 2+ spaces to 1 space: (May  2 -> May 2)
            if all(string in i for string in ['Failed password', IP]):  # parse failed logins (invalid user
                if 'invalid user' in i:                                 # or password) and add to list
                    user = re.findall('invalid user (.*) from', i)[0]
                else:
                    user = re.findall('password for (.*) from', i)[0]
                failedUsersList.append(user)

            if all(string in i for string in ['Accepted password', IP]): # parse successful logins and add to list
                user = re.findall('password for (.*) from', i)[0]
                timestamp = ' '.join(i.split(' ', 3)[:3])
                successfulLogins[user] = timestamp


        for username in failedUsersList:                                # add failed logins to activity dict
            if username not in failedUsers.keys():
                failedUsers[username] = failedUsersList.count(username)

    activity['source_ip'] = IP                                          # create dictionary object from parsed info
    activity['failed_logins'] = failedUsers
    activity['total_fails'] = len(failedUsersList)
    if len(successfulLogins) > 0:
        activity['successful_logins'] = successfulLogins
    else:
        activity['successful_logins'] = 0

    return activity

def parseLogs():                            # Parse all IPs
    ipList = extractIPs()
    for IP in ipList:
       activity.append(findActivity(IP))
    print(json.dumps(activity))


parseLogs()
