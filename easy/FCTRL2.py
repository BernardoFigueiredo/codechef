#Small factorials
#http://www.codechef.com/problems/FCTRL2

import array
import sys

a = array.array('i', (-1 for i in range(101)))
a[1] = 1

def fact(n):

  if a[n] == -1:
    return n * fact(n-1)

  return a[n]
  


t = int(input())

for i in range(t):
  n = int(input())
  print(fact(n))




