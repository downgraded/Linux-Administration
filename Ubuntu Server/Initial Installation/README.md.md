# Ubuntu Server Installation (1/27/2021)
> Documentation of the initial setup of the server
---
## Installation:
1. Download Ubuntu Server iso from https://ubuntu.com/download/server (Option 2: Manual server installation)
2. In VMWare, create a new virtual machine and use the "typical" configuration
3. Select the "Installer disc image file (iso)" option and select the Ubuntu Server iso. VMWare will detect the OS and use "Easy Install"
4. Click next, and enter a name, username, and password to be used
5. Continue forward with the default options until finished
6. Power on the virtual machine
7. When prompted, select English, and continue through with the default options by pressing "Done" until reaching "Profile setup"
8. Enter a server name, a username, and password
9. Do not install OpenSSH for now, or any server snaps
10. The system will begin installation
11. Once the installation is finished (it will say "Installation Complete!" at the top), click reboot

## Configuration Changes:
Changes made to configurations immediately following initial installation

#### SSH Install
> Install OpenSSH server and client to allow ssh access to and from other machines on the network

As root: 
- Install openssh server and openssh client with `apt install openssh-server openssh-client`
- Start SSH daemon: `systemctl start sshd`
- Enable SSH daemon: `systemctl enable sshd`

#### Create Sudo User
> Create a user with sudo privileges to be used for SSH

As root:
Add the user account created during initial installation to the sudo group with: `usermod -aG sudo <username>`