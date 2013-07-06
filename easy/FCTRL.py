#Factorial
#http://www.codechef.com/problems/FCTRL

def z(n):
    return (n//5 + n//25 + n//125 + n//625 + \
            n//3125 + n//15625 + n//78125 + \
            n//390625 + n//1953125 + n//9765625 + \
            n//48828125 + n//244140625)

t = int(input())
for i in range(t):
    n = int(input())
    print(z(n))

