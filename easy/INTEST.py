#Enormous Input Test
#http://www.codechef.com/problems/INTEST

import sys

num_to_read = 65536

i = sys.stdin.readline()
i = i.split(" ")
n = int(i[0])
k = int(i[1])

count = 0
exit = 0
while not exit:
    l = sys.stdin.readlines(num_to_read)
    for i in range(num_to_read):
        if int(l[i]) % k == 0:
            count += 1
        n -= 1
        if n == 0:
            exit = 1
            break
    

print(count)


