def shash1(x):
	return x

def shash2(x, y):
	return x + (x + y)*(x + y + 1)/2

def shash3(x, y, z):
	return x + (x + y)*(x + y + 1)/2 + (x + y + z)*(x + y + z + 1)*(x + y + z + 2)/6

def shashn(*v):
	r = 0
	f = 1
	n = len(v)

	for i in range(1, n + 1):
		s = 0
		for c in range(i):
			s += v[c]

		t = s
		for c in range(1, i):
			t *= s + c

		f *= i
		r += t/f

	return r
