import math

# Runtime: 40 ms
# Memory Usage: 13.8 MB
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1: return True
        if num < 1: return False

        return math.floor(math.log(num,4)) == math.ceil(math.log(num,4))


#### Alternative solutions
# Runtime: 56 ms
def isPowerOfFour(self, num):
  if num<1:
      return False
  x = log(num)/log(4)
  return  x == int(x)


# Runtime: 40 ms
def isPowerOfFour(self, num: int) -> bool:
    return num > 0 and (num & (num-1)) == 0 and (num-1) % 3 == 0

# Runtime: 36 ms
def isPowerOfFour(self, num: int) -> bool:
  bin_str = bin(num)
  bin_str = list(bin_str[2:])
  return bin_str.count("1") == 1 and bin_str[0] == "1" and bin_str.count("0") %2==0

# Runtime: 32 ms
# most popular solution
def isPowerOfFour(self, num: int) -> bool:
  if num < 1:
      return False
  return num & (num - 1) == 0 and num == int(num & int('0x555555555', 16))

# Runtime: 28 ms
# Doesn't meet requirement to solve without loops/recursion
def isPowerOfFour(self, num: int) -> bool:
  n=num
  if n == 1:
      return True
  while n>1:
      if n%4 == 0:
          n = n//4
      else:
          return False
      if n == 1:
          return True

# Runtime: 20 ms
def isPowerOfFour(self, num: int) -> bool:
  if num==0:
      return False
  return (num & num-1==0) & len(bin(num))%2==1

# Runtime: 16 ms
def isPowerOfFour(self, num):
  if num<= 0:
      return False
  z = bin(num)[::-1]
  if z.count('1') > 1:
      return False
  p = z.index('1')
  return p % 2 == 0

# Runtime: 12 ms
# Doesn't meet requirement to solve without loops/recursion
def isPowerOfFour(self, n: int) -> bool:
  if n < 1:
      return False
  while n%4 == 0:
      n /= 4
  return True if n==1 else False


# Memory Usage: 13.8 MB
def isPowerOfFour(self, num: int) -> bool:
  if num <= 0:
      return False
  else:
      while num % 4 == 0:
          num /= 4
      return True if num == 1 else False
                
# Memory Usage: 13.6 MB
def isPowerOfFour(self, num: int) -> bool:
  for i in range(0, 32):
      if (4 ** i) == num:
          return True
  return False