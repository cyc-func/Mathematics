p1 = '0'
p2 = '1'

for x in xrange(6):
	p3 = 'd*(' + p2 + ')' + '+' + p1
	p1 = p2
	p2 = p3

print p1
