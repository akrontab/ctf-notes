# gitMeow - Misc

## Description

Just another annoying git challenge :)

Author: zAbuQasem

nc 172.190.120.133 50001

## Solution

We are given a prompt to enter git commands. After some trial and error we can see that the `git grep` command is allowed. Knowing the flag format is `0xL4ugh{something}` we can use `grep ugh` and that should find all files that have the string `ugh` and should print out the flag.

```bash
┌──(kali㉿kali)-[~/Desktop/git]
└─$ nc 172.190.120.133 50001

 _____ _ _  ___  ___                   
|  __ (_) | |  \/  |                   
| |  \/_| |_| .  . | ___  _____      __ 
| | __| | __| |\/| |/ _ \/ _ \ \ /\ / / 
| |_\ \ | |_| |  | |  __/ (_) \ V  V /  
 \____/_|\__\_|  |_/\___|\___/ \_/\_/   

[+] Welcome challenger to the epic GIT Madness, can you read /flag.txt?
Enter git commands (Enter an empty line to end):
grep ugh 

flag.txt:0xL4ugh{GiT_D0c3_F0r_Th3_WiN}

```

Flag: `0xL4ugh{GiT_D0c3_F0r_Th3_WiN}`