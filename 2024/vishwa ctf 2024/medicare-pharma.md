# MediCare Pharma - Web

## Description

Greetings form MediCare Pharma!!!!

We have started a very new pharmacy where we have various surgical equipments (more to be added soon).

But recently some hackers took control of our server and changed a hell lot of things (probably wiped out everything). Luckily we have few of the accounts and we need more consumers on board. For security reasons, we have disabled SignUp, only authorised persons are allowed to login.

Have a look at our pharmacy and hope we grow again soon.

Author : Ankush Kaudi

FLAG FORMAT:
VishwaCTF{}

## Solution

<https://ch491695148735.ch.eng.run/>

```bash
┌──(kali㉿kali)-[~]
└─$ nmap -Pn ch491695148735.ch.eng.run
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-01 22:08 EST
Nmap scan report for ch491695148735.ch.eng.run (13.232.183.110)
Host is up (0.29s latency).
Other addresses for ch491695148735.ch.eng.run (not scanned): 3.7.241.93 13.232.112.2
rDNS record for 13.232.183.110: ec2-13-232-183-110.ap-south-1.compute.amazonaws.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https
```
