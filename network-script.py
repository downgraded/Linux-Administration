import subprocess
import re
import sys
import json

# Create arguments
if len(sys.argv) >= 2:
    print(sys.argv[1])

# Parse command and capture output
def runCommand(cmd):
    command = []
    for i in cmd.split(): #Ex: "ip -j a" -> "['ip', '-j', 'a']"
        command.append(i)
    output = subprocess.run(command, capture_output=True).stdout.decode()
    return output

# Get IP Info
ip = []
cmd = "ip -j a" # output as JSON for easier parsing
ipOutput = runCommand(cmd)

# Parse IP output
ipOutput = json.loads(ipOutput) 
numInts = len(ipOutput) # number of interfaces

def parseInterface(i):
    addrs = {}
    interface = ipOutput[i]
    name = interface['ifname']
    flags = interface['flags']
    state = interface['operstate']
    intDict = {
            "name":name,
            "flags":flags,
            "state":state
            }
    addr_info = interface['addr_info']
    numAddrs = len(addr_info)
    for i in range(numAddrs):
        addr_type = addr_info[i]['family']
        addr = addr_info[i]['local']
        life_time = addr_info[i]['valid_life_time']
        if life_time == 4294967295:
            life_time = 'forever'
        else:
            pass
        addrs[i] = [addr_type, addr, life_time]
        intDict[i] = addrs[i]
    return intDict


for i in range(numInts):
    ip.append(parseInterface(i))

# Get open port info
ports = [] # todo: change to dict
cmd = "netstat -tunlp"
portOutput = runCommand(cmd)

# Parse port output
def parseLine(line):
    proto = line.split()[0]
    port = line.split()[3].split(':')[-1]
    pid = line.split()[-1]
    if len(line.split()) == 6:
        state = "LISTENING"
    else:
        state = "NOT LISTENING"
    output = f"{proto} {port} {pid} {state}"
    return output

for i in portOutput.splitlines()[2:]:
    ports.append(parseLine(i))

# Get Others
# ubuntu-server: /etc/netplan/00-installer-config.yaml
# centos: /etc/sysconfig/network-scripts/ifcfg-ens33
host = runCommand('hostname')



if host == 'ubuntu-server':
    getUbuntuConfig()
elif host == 'CentOS':
    getCentOSConfig()