# Baby Jail - Misc

## Description

Just a baby jail. Nothing special!

nc dyn.ctf.pearlctf.in 30017

## Solution

This is a simple jail break challenge that uses python's `eval()` evaulate the command given from the input. We are given the following source code for the jail:

```python
#!/usr/local/bin/python
import time
flag="pearl{f4k3_fl4g}"
blacklist=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`![]{},<>/123456789")
def banner():
    file=open("txt.txt","r").read()
    print(file)
def check_blocklist(string):
    for i in string:
        if i in blacklist:
            return(0)
    return(1)
def main():
    banner()
    cmd=input(">>> ")
    time.sleep(1)
    if(check_blocklist(cmd)):
        try:
            print(eval(cmd))
        except:
            print("Sorry no valid output to show.")
    else:
        print("Your sentence has been increased by 2 years for attempted escape.")

main()
```

We can see the blacklist is restricting the use of all characters of the format `\w` and `\d` along with a few special characters. The shortest path to the flag would be to have it execute `print(flag)` but this doesn't pass the filter. Lucky for us, Python will normalize fonts so we can pass in the characters in italics and this will bypass the filter. This site can be used to generate italicized text <https://lingojam.com/ItalicTextGenerator>

```bash
┌──(kali㉿kali)-[~]
└─$ nc dyn.ctf.pearlctf.in 30017
ooooooooo.   oooooooooooo       .o.       ooooooooo.   ooooo        
`888   `Y88. `888'     `8      .888.      `888   `Y88. `888'        
 888   .d88'  888             .8"888.      888   .d88'  888         
 888ooo88P'   888oooo8       .8' `888.     888ooo88P'   888         
 888          888    "      .88ooo8888.    888`88b.     888         
 888          888       o  .8'     `888.   888  `88b.   888       o 
o888o        o888ooooood8 o88o     o8888o o888o  o888o o888ooooood8 

>>> 𝘱𝘳𝘪𝘯𝘵(𝘧𝘭𝘢𝘨)
pearl{it_w4s_t00_e4sy}
None
```

FLAG: `pearl{it_w4s_t00_e4sy}`
