def f(y, n):
	expr = y
	for x in xrange(n-1):
		expr = expr.replace('x', y)
	return expr

print f('(x+b)/(x+d)', 4)
