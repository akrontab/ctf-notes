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
pattern = '\d+'
out = []

numbers = re.findall(pattern, flag)

for s in numbers:
	num = int(s)
	i = int(random.choice(ops)(num))
	out.append(chr(i))

print(''.join(out))