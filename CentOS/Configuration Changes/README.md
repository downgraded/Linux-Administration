# CentOS Configuration Changes
> Documentation of all additional altered configurations on the CentOS server beyond initial setup
---

#### Fail2ban
Changes to the default configuration of the fail2ban service to enable for ssh 
Changes: 
##### /etc/fail2ban/jail.local:
copy jail.conf to jail.local and change settings
```bash
sudo su -
cd /etc/fail2ban
cp jail.conf jail.local
vim jail.local 	# uncomment ignoreip and add my host ip \
				# change maxretry from 5 to 3
```

##### /etc/fail2ban/jail.d/sshd.local
```bash
cd /etc/fail2ban/jail.cd
touch sshd.local && chmod +x sshd.local
vim sshd.local # enter the below code
```
```
[sshd] 
enabled = true 
port = ssh 
#action = firewallcmd-ipset 
logpath = %(sshd\_log)s 
maxretry = 3 
bantime = 86400
```

Start/enable fail2ban with: `systemctl start fail2ban` & `systemctl enable fail2ban`

Verify fail2ban is working by failing an SSH login from an unignored ip, then checking ssh jail status with: `fail2ban-client status sshd`

---

#### Static IP
Giving the server a static IP address
Changes: 
##### /etc/sysconfig/network-scripts/ifcfg-ens33
- Change `BOOTPROTO` from `dhcp` to `none`
- Add the follwing lines: 
```
IPADDR=192.168.1.4 # static IP for the server
PREFIX=24 # 24 bit subnet
GATEWAY=192.168.1.1 # router IP
DNS=192.168.1.6 # DNS server IP (pihole)
```

---

#### Host Changes
Configuration changes on my host related to the server
Changes:
##### /etc/hosts (C:\\Windows\\System32\\drivers\\etc\\hosts)
> (temporary workaround until I figure out the issue)
>
> Add an entry to my etc\\hosts file so I can access the server via hostname rather than just IP address (ex: ping CentOS vs ping 192.168.1.4)
- Add the following line to C:\\Windows\\System32\\drivers\\etc\\hosts:
`192.168.1.4	CentOS`
