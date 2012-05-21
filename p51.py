import sys
from math import sqrt

def isPrime(n):
  i = 2
  while i <= sqrt(n):
    if n % i == 0:
      return False
    i += 1
  return True

def replaceDigit(number, positions):
  ret = []
  i = 0
  s = list(str(number))
  while i < 10:
    for position in positions:
      s[position] = str(i)
    ret[len(ret):] = [int("".join(s))]
    i += 1
  return ret

def _subsetOfSizeK(k, n):
  if k == 0 or n < k:
    yield set()
  elif n == k:
    yield set(range(n))
  else:
    for s in _subsetOfSizeK(k-1,n-1):
      s.add(n-1)
      yield s
    for s in _subsetOfSizeK(k,n-1):
      yield s

def allindices(string, sub, listindex=[], offset=0):
  i = string.find(sub, offset)
  while i >= 0:
    listindex.append(i)
    i = string.find(sub, i + 1)
  return listindex

def subsetOfSizeK(k,number):
  if k == 0 or len(str(number)) < k:
    yield set()
  elif len(str(number)) == k:
    s = set(list(str(number)))
    if len(s) == 1:
      yield set(range(len(str(number))))
    else:
      yield set()
  elif k == 1:
    for i in range(len(str(number))):
      yield set([i])
  else:
    cs = list(str(number))
    for c in set(cs):
      indices = allindices(str(number),c,[])
      if len(indices) == k:
        yield set(indices)
      elif len(indices) > k:
        #subs = _subsetOfSizeK(k,len(indices))
        print(len(indices), c, number)
        for sub in _subsetOfSizeK(k,len(indices)):
          ss = set()
          for s in sub:
            ss.add(indices[s])
          yield ss
      

def replaceNDigits(number, n, familySize, ps):
  sub = subsetOfSizeK(n,number)
  for s in sub:
    sys.stdout.write(str(number) + ": " + str(s) + ": ")
    nums = replaceDigit(number, s)
    c, primes = countPrimes(nums,number,ps)
    ps |= primes
    if c == familySize:
      return familySize, ps
    sys.stdout.write("\n")
  return 0, ps

def replaceDigits(number,familySize, ps):
  n = len(str(number))
  i = 1
  while i < n:
    c, ps = replaceNDigits(number, i, familySize, ps)
    if familySize == c:
      return familySize, ps
    i += 1
  return 0, ps

def countPrimes(ps,number,primes):
  s = 0
  l = len(str(number))
  for p in ps:
    if l == len(str(p)) and (p in primes or isPrime(p)):
      sys.stdout.write(str(p) + ", ")
      s += 1
      primes.add(p)
  return s, primes

def smallestPrimeFamily(n):
  i = 3
  s = 0
  ps = set()
  while s != n:
    if isPrime(i):
      s,ps = replaceDigits(i,n,ps)
    i += 2
  sys.stdout.write("\n")

