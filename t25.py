l = 10 ** 999;

x1 = 1;
x2 = 1;
k = 0;

while (x2 < l):
	k = x1 + x2;
	x1 = x2;
	x2 = k;

print(x2);