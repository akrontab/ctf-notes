# baby-rev

## Description

anita max wyinn

4rm44n

## Solution

```bash
 ┌──(kali㉿kali)-[~/Desktop/babyrev]
└─$ file baby-rev 
baby-rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=995dafe783aef67cc95910e4f3c2a0152eeb34c0, for GNU/Linux 3.2.0, not stripped
```

If we use Ghidra to analyze the file we can see this code in the main function

```C
  printf("Enter a string: ");
  fgets(userInput,32,stdin);
  sVar1 = strlen(userInput);
  if (sVar1 == 24) {
    myfunc(userInput);
  }
  else {
    puts(":P\n");
```

If we enter a string that is 23 characters + the newline character we should execute `myfunc()` which looks like the following:

```C
void myfunc(char *inputStr)

{
  if (*inputStr == 'B') {
    if (((((((inputStr[4] == 'C') && (inputStr[13] == 'm')) && (inputStr[19] == 'r')) &&
          (((inputStr[3] == 'S' && (inputStr[10] == 'l')) &&
           ((inputStr[2] == 'T' && ((inputStr[14] == 'e' && (inputStr[17] == '0')))))))) &&
         ((inputStr[22] == '}' &&
          (((inputStr[7] == '{' && (inputStr[5] == 'T')) && (inputStr[15] == '_')))))) &&
        (((inputStr[1] == 'I' && (inputStr[21] == 'v')) &&
         (((inputStr[8] == 'w' && ((inputStr[11] == 'c' && (inputStr[6] == 'F')))) &&
          (inputStr[20] == '3')))))) &&
       ((((inputStr[9] == '3' && (inputStr[12] == '0')) && (inputStr[16] == 't')) &&
        (inputStr[18] == '_')))) {
      puts("Yippee :3\n");
    }
  }
  else {
    puts(":PP\n");
  }
  return;
}
```

At this point it's a matter of reversing what the inputStr character indexes are. Which is:

Flag: `BITSCTF{w3lc0me_t0_r3v}`
