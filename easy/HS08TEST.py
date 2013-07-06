#ATM
#http://www.codechef.com/problems/HS08TEST

bank_charge = 0.50

s = input()
s = s.split(" ")
x = int(s[0])
y = float(s[1])

if (x % 5) == 0:
    if x + bank_charge <= y:
        y -= x + bank_charge

print('{:.2f}'.format(y))
