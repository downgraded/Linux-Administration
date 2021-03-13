# CentOS Installed Packages
> Documentation of all additional installed programs/packages on the CentOS server beyond initial setup
---
## Packages:
---
##### GCC (gnu compiler collection) 
/usr/bin/gcc

Date: 2/3/2021
Reason for installation: compiling source code of `sudo-1.9.5p2` for installation
Installed via: `sudo yum install gcc`
---
##### Make
/usr/bin/make

Date: 2/3/2021
Reason for installation: compiling source code of `sudo-1.9.5p2` for installation
Installed via: `sudo yum install gcc`

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
Installed via: `yum install tmux`

---
##### emacs
/usr/bin/emacs

Date: 3/3/2021
Reason for installation: Text editor, alternative to vim
Installed via: `yum install emacs`

---
##### Fail2Ban & EPEL (Extra Packages for Enterprise Linux)
/etc/fail2ban/

Date: 3/3/2021
Reason for installation: Prevent bruteforcing by temporarily ban hosts after too many failed login attempts
Installed via: 
```bash
yum install epel-release # install EPEL repository
yum install fail2ban fail2ban-systemd
```

---
##### cowsay
/usr/bin/cowsay

Date: 3/3/2021
Reason for installation: Echo text in ascii art cow speech bubble (just for fun)
Installed via: `yum install cowsay` (also installed from EPEL repo)

---
##### Ruby
/usr/bin/ruby

Date: 3/3/2021
Reason for installation: Usage of `lolcat`
Installed via: `yum install ruby`
---
	
##### lolcat
/usr/games/lolcat

Date: 3/3/2021
Reason for installation: Cat files or show stdout in rainbow colors (just for fun)
Installed via: 
```bash
wget https://github.com/busyloop/lolcat/archive/master.zip
unzip master.zip
cd lolcat-master/bin
gem install lolcat
```

---
##### Requests (python library)
/usr/lib/python3/dist-packages/requests/

Date: 3/8/2021
Reason for installation: Python library for performing web requests
Installed via: `pip install requests`
