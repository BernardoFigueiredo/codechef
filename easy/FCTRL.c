#Factorial
#http://www.codechef.com/problems/FCTRL

#include<stdio.h>

int z(int n)
{
	return (n/5 + n/25 + n/125 + n/625 + n/3125 + n/15625 + n/78125 + n/390625 + n/1953125 + n/9765625 + n/48828125 + n/244140625);
}

int main(int argc, char ** argv)
{
	int t, i, n;
	
	t = scanf("%d", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%d", &n);
		printf("%d\n", z(n));
	}
	
	return 0;
}