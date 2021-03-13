# Ubuntu Server Installed Packages
> Documentation of all additional installed programs/packages on the Ubuntu-Server server beyond initial setup
---
## Packages:
---
##### GCC (gnu compiler collection) 
/usr/bin/gcc

Date: 2/3/2021
Reason for installation: compiling source code of `sudo-1.9.5p2` for installation
Installed via: `sudo apt install gcc`

---
##### Make
/usr/bin/make

Date: 2/3/2021
Reason for installation: compiling source code of `sudo-1.9.5p2` for installation
Installed via: `sudo apt install gcc`

---
##### Sudo 1.9.5p2
/usr/local/bin/sudo

Date: 2/3/2021
Reason for installation: Patching CVE-2021-3156: Heap-Based Buffer Overflow in Sudo (Baron Samedit) 
Installed via: 

```bash
wget https://www.sudo.ws/dist/sudo-1.9.5p2.tar.gz
tar xzvf sudo-1.9.5p2.tar.gz
cd sudo-19.5p2
./configure
make && sudo make install
mv ./sudo /usr/local/bin/sudo
```

---
##### Tmux
/usr/bin/tmux

Date: 3/2/2021
Reason for installation: Extra utility in command line
Installed via: `sudo apt install tmux`

---
##### emacs
/usr/bin/emacs

Date: 3/3/2021
Reason for installation: Text editor, alternative to vim
Installed via: `sudo apt install emacs`

---

##### Fail2Ban
/etc/fail2ban/

Date: 3/3/2021
Reason for installation: Prevent bruteforcing by temporarily ban hosts after too many failed login attempts
Installed via: `sudo apt install fail2ban`

---
##### cowsay
/usr/bin/cowsay

Date: 3/3/2021
Reason for installation: Echo text in ascii art cow speech bubble (just for fun)
Installed via: `sudo apt install cowsay`

---
##### cowsay
/usr/bin/cowsay

Date: 3/3/2021
Reason for installation: Echo text in ascii art cow speech bubble (just for fun)
Installed via: `yum install cowsay` (also from EPEL repo)

---
##### Ruby
/usr/bin/ruby

Date: 3/3/2021
Reason for installation: Usage of `lolcat`
Installed via: `sudo apt install ruby`

---
##### lolcat
/usr/games/lolcat

Date: 3/3/2021
Reason for installation: Usage of `lolcat`
Installed via: `sudo apt install lolcat`

---