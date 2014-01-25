def get_sum(n):
	if n == 0: 
		return 1;
	
	top_right = (2 * n + 1) ** 2;
	bottom_left = (2 * n + 1) ** 2 - 4 * n;
	top_left= top_right - 2 * n;
	bottom_right = bottom_left - 2 * n;
	return top_right + bottom_left + top_left + bottom_right;

def get(n):
	s = 0;
	for i in range(0, n + 1):	
		s += get_sum(i);
	return s;

print(get(500));