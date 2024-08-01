# TerraMeow - MISC

## Description

Easy challenge to get you learn basics of IAC with Terraform.

Author: zAbuQasem

nc 172.190.120.133 50002

## Solution

This was a pretty simple challenge if you have some knowledge of terraform. We are given the `.tf` files for the challenge and see that there is a variable named `FLAG`. We also see in the challenge script that if the flag is in the output then we get a monkey as the output an no flag. So we need a terraform function that modified the variable value in some way.

After checking the Terraform console function docs we see there is a function called `strrev` which reverses the value it's given. Why you would even need this in an IaC tool is beyond me, but a flag is a flag, so let's give it a try.

```bash
┌──(kali㉿kali)-[~/Desktop/terraform]
└─$ nc 172.190.120.133 50002                

 _____                  ___  ___                   
|_   _|                 |  \/  |                   
  | | ___ _ __ _ __ __ _| .  . | ___  _____      __ 
  | |/ _ \ '__| '__/ _` | |\/| |/ _ \/ _ \ \ /\ / / 
  | |  __/ |  | | | (_| | |  | |  __/ (_) \ V  V /  
  \_/\___|_|  |_|  \__,_\_|  |_/\___|\___/ \_/\_/   

[+] Welcome challenger to the epic IAC Madness
Enter terraform console commands (Enter an empty line to end):
strrev(var.FLAG)

"}3t4T_0rDnA_3t4Ts_fT{hgu4Lx0"
                                                                                                                         
┌──(kali㉿kali)-[~/Desktop/terraform]
└─$ echo "}3t4T_0rDnA_3t4Ts_fT{hgu4Lx0" | rev
0xL4ugh{Tf_sT4t3_AnDr0_T4t3}

```

Flag:  `0xL4ugh{Tf_sT4t3_AnDr0_T4t3}`
