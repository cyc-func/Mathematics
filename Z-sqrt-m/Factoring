def isUnit(a, b, m):
  norm = a*a - m*b*b
  if norm == 1 or norm == -1:
    return True
  return False

def isPrime(a, b, m):       # 1 is treated as prime
  norm = a*a - m*b*b
  if norm < 0:
    norm = -norm
  if norm == 1 or norm == 2:
    return True
  for x in xrange(2, int(norm ** 0.5) + 2):
    if norm % x == 0:
      return False
  return True

def test(ac, bd, y, m):
  for i in xrange(1, ac + 1):
    if ac % i == 0:
      a = i
      c = ac / i
      for j in xrange(1, bd + 1):
        if bd % j == 0:
          b = j
          d = bd / j

          if (b*c - a*d == y) and (not isUnit(a, b, m)) and (not isUnit(c,d,m)):
            print '(',a,'+',b,u'\u221A',m,')', '(',c,'-',d,u'\u221A',m,')'
            return False

  return True

def factor(x, y, m):     # factor x + y*sqrt(m)
  # (a + b*sqrt(m))(c - d*sqrt(m)) = ac - mbd + (bc - ad)*sqrt(m)
  # ac - mbd = x
  # bc - ad  = y
  ac = x + m
  bd = 1

  while test(ac, bd, y, m):
    ac += m
    bd += 1

p = 9
q = 2
r = 5

if isPrime(p,q,r):
  print 'Cannot be factored'
else:
  factor(p, q, r)
