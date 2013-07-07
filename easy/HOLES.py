#Holes in the text
#http://www.codechef.com/problems/HOLES

n = int(input())

for i in range(n):
  count = 0
  line = input()
  l = len(line)
  for j in range(l):
    if line[j] in ('A', 'D', 'O', 'P', 'R', 'Q'):
      count += 1
    elif line[j] == 'B':
      count += 2
  print(count)
