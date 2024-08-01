# not quite caesar - crypto

## Description

Caesar??? Couldn't be this!

## Solution

We are given two files: a python script and a text file

**nqc.py**

```python
import random
random.seed(1337)
ops = [
    lambda x: x+3,
    lambda x: x-3,
    lambda x: x*3,
    lambda x: x^3,
]

flag = list(open("out.txt", "rb").read())
out = []
for v in flag:
    out.append(random.choice(ops)(v))
print(out)
```

**out.txt**

```text
[354, 112, 297, 119, 306, 369, 111, 108, 333, 110, 112, 92, 111, 315, 104, 102, 285, 102, 303, 100, 112, 94, 111, 285, 97, 351, 113, 98, 108, 118, 109, 119, 98, 94, 51, 56, 159, 50, 53, 153, 100, 144, 98, 51, 53, 303, 99, 52, 49, 128]
```

The text file gives out the output of the script when `flag` is the input.  Also notice that the seed is hard coded when using `random` so this should be pretty simple to reverse the basic encryption. For each of the `ops` we need to arrange them so the reverse operation is in place of the original. That gives us this the list

```python
ops = [
    lambda x: x-3,
    lambda x: x+3,
    lambda x: x/3,
    lambda x: x^3,
]
```

Next step is to read and parse `out.txt` so we get a list of integers. Once we have the ints we can apply the reverse operation using the same seed value when initializing `random`.  Finally the quick and dirty script to solve the challenge is below:

```python
import random
import re
random.seed(1337)
ops = [
    lambda x: x-3,
    lambda x: x+3,
    lambda x: x/3,
    lambda x: x^3,
]

flag = open("out.txt", "r").read()
numbers = []
out = []
pattern = '\d+'

numbers = re.findall(pattern, flag)

for s in numbers:
    num = int(s)
    i = int(random.choice(ops)(num))
    out.append(chr(i))

print(''.join(out))
```

FLAG: `vsctf{looks_like_ceasar_but_isnt_a655563a0a62ef74}`