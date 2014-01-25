
x1 = 1;
x2 = 1;
s = 2;
while x2 < 4 * (10 ** 6):
	k = x2 + x1;
	x1 = x2;
	x2 = k;
	if x2 % 2 == 0:
		s += x2

print(s);