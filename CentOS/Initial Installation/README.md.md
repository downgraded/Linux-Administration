# CentOS Installation (1/27/2021)
> Documentation of the initial setup of the server

[x86_64 ISO](http://isoredirect.centos.org/centos/8/isos/x86_64/)

--- 
## Installation:
1. Download CentOS iso from https://www.centos.org/download/
2. In VMWare, create a new virtual machine and use the "typical" configuration
3. Select the "Installer disc image file (iso)" option and select the CentOS iso
4. Select the correct operating system (Linux, CentOS 8 64-bit)
5. Continue forward with the default options until finished
6. Power on the virtual machine
7. When prompted, select the appropriate language options (Should be English by default)
8. The installation summary will appear (for whatever reason it is cut off, but that doesn't matter) ![[Pasted image 20210312000920.png]]
9. Click on "Root Password" to set a root password
10. Click on "Network and Host Name" and turn on the network interface ![[Pasted image 20210312000935.png]]
11. Click on "Installation Destination" to select the VMWare disk
12. Find a CentOS mirror from somewhere geographically close at https://www.centos.org/download/mirrors/ (Harvard SEAS mirror: http://mirrors.seas.harvard.edu/centos/8.3.2011/BaseOS/x86\_64/os/)
13. Click on "Installation Source" and type the link to the mirror. Click "Done” and wait for the download to finish ![[Pasted image 20210312000953.png]]
14. Click on "Software Selection" and select "Server" as the Base Environment.
15. After everything in the Installation Summary has been set, click "Begin Installation" in the bottom right, and wait
16. Once installation is complete, click "Reboot System"
17. In VMWare, click the "Finished Installing" button
18. Login to the server as root with the password that was set during Step 9
---
## Configuration Changes:
Changes made to configurations immediately following initial installation

#### SSH Install
> Install OpenSSH server and client to allow ssh access to and from other machines on the network

As root:
- Install openssh server and openssh client with: `yum install openssh-server openssh-client`
- Start SSH daemon: `systemctl start sshd`
- Enable SSH daemon: `systemctl enable sshd`

#### Create Sudo User
> Create a user with sudo privileges to be used for SSH

As root:
- Create user account with: `adduser <username>`
- Add user to the `wheel` group with: `usermod -aG sudo <username>`