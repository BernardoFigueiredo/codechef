import sys

l = sys.stdin.readlines()
j = l[0]
l = l[1:]
l[-1] = l[-1] + "\n"
l.sort(key=lambda x: int(x))
s = ""

for i in range(int(j)):
  s += l[i]

print(s[:-1])