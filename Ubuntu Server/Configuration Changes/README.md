# Ubuntu Server Configuration Changes
> Documentation of all additional altered configurations on the Ubuntu Server server beyond initial setup
---

#### Fail2ban
Changes to the default configuration of the fail2ban service to enable for ssh 
Changes: 
##### /etc/fail2ban/jail.local:
create new file /etc/fail2ban/jail.local and enter the following lines:
```
[sshd]
enabled = true
port = 22
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
ignoreip = 192.168.1.2 # my host ip
```

Restart/enable fail2ban with: `sudo systemctl restart fail2ban` & `sudo systemctl enable fail2ban`

Verify fail2ban is working by failing an SSH login from an unignored ip, then checking ssh jail status with: `sudo fail2ban-client status sshd`

---
#### Static IP
Giving the server a static IP address
Changes: 
##### /etc/netplan/00-installer-config.yaml
- change `dhcp4: True` to `dhcp4: no`
- add the following lines:
```
addresses:
  - 192.168.1.12/24
gateway4: 192.168.1.1
nameservers:
		addresses: [192.168.1.6, 8.8.8.8]
```

The config should now look like:
```
# This is the network config written by 'subiquity'
network:
  ethernets:
    ens33:
      dhcp4: no
      addresses:
        - 192.168.1.12/24
      gateway4: 192.168.1.1
      nameservers:
              addresses: [192.168.1.6, 8.8.8.8]
  version: 2
```

Apply changes with: `sudo netplan apply`

---

#### Host Changes
Configuration changes on my host related to the server
Changes:
##### /etc/hosts (C:\\Windows\\System32\\drivers\\etc\\hosts)
> (temporary workaround until I figure out the issue)
>
> Add an entry to my etc\\hosts file so I can access the server via hostname rather than just IP address (ex: ping ubuntu-server vs ping 192.168.1.12)
- Add the following line to C:\\Windows\\System32\\drivers\\etc\\hosts:
`192.168.1.12	ubuntu-server`
