# Golden Gate 

## Description

Nah, this isn’t ssh, so what? We’ve been using telnet for years, there’s no reason to switch.

Update on February 11, 00:25: The system administrator has updated the system configuration, but made a critical mistake. Can you find what went wrong?

telnet goldengate.q.2024.ugractf.ru 9277 -l jf2ut2vh2uwnkexv
Login: ugra
Password: ucucuga

Challenge by purplesyringa.

## Solution

```bash
/ $ ls
auth.sh  etc      lib      opt      run      sys      var
bin      flag     media    proc     sbin     tmp
dev      home     mnt      root     srv      usr
/ $ ls -l
total 60
-rwxr-xr-x    1 root     root           341 Feb 10 19:19 auth.sh
drwxr-xr-x    2 root     root          4096 Feb 10 07:57 bin
drwxr-xr-x    1 root     root           320 Feb 10 19:57 dev
drwxr-xr-x    1 root     root          4096 Feb 10 07:57 etc
-r--------    1 root     root            68 Feb 10 19:57 flag
drwxr-xr-x    1 root     root            60 Feb 10 06:32 home
drwxr-xr-x    7 root     root          4096 Jan 26 17:53 lib
drwxr-xr-x    5 root     root          4096 Jan 26 17:53 media
drwxr-xr-x    2 root     root          4096 Jan 26 17:53 mnt
drwxr-xr-x    2 root     root          4096 Jan 26 17:53 opt
dr-xr-xr-x  959 nobody   nobody           0 Feb 10 19:57 proc
drwx------    2 root     root          4096 Jan 26 17:53 root
drwxr-xr-x    1 root     root            40 Jan 26 17:53 run
drwxr-xr-x    2 root     root          4096 Jan 26 17:53 sbin
drwxr-xr-x    2 root     root          4096 Jan 26 17:53 srv
drwxr-xr-x    2 root     root          4096 Jan 26 17:53 sys
drwxrwxrwt    1 root     root            40 Jan 26 17:53 tmp
drwxr-xr-x    7 root     root          4096 Jan 26 17:53 usr
drwxr-xr-x   12 root     root          4096 Jan 26 17:53 var
```

