Install MogileFS on Debian
==========================

Create
------
Create a virtual machine with Debian.

Hostname
--------
The MogileFS server needs a fixed ip or hostname reachable from the outside.
Simple solution is to install `avahi-daemon`

```bash
apt-get install avahi-daemon
```

and use `$host.local`, where `$host` is you local machine name.

Install
-------
Copy the files in this directory to the server.
Login as root an run (typing in yes when needed) replacing `$host` with your hostname or ip:

```bash
./01-install
./02-start-tracker
./03-configure $host
./04-start-storage
./05-check
```

You system is now installed and running.

Domain
------
You can add a domain as follows (replace $domain with the domain):

```bash
mogadm domain add $domain
```

Run
---
If you need to run MogileFS after reboot do:
```bash
./02-start-tracker
./04-start-storage
./05-check
```
