# По данному натуральному n определите количество последовательностей длины n из 0 и 1, не содержащих двух единиц подряд. Гарантируется, что ответ не превосходит 2^31 - 1.



def solve(n):
  sequence_count = 1 + n # case when all zeroes + cases when only 1 is the number
  print('n', n, sequence_count)


# ======== main

solve(2)
# if n = 2, then answer = 3 = 1 + 2
# 1 0 
# 0 1
# 0 0

# if n = 3, then answer = 5 = 1 + 3 + 1
# 0 0 0
# 1 0 0
# 0 0 1
# 0 1 0

# 1 0 1


# if n = 4, then answer = 1 ( all zeroes) + n ( one 1 and others are zeroes) + 3

# 0 0 0 0
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# 1 0 1 0
# 1 0 0 1
# 0 1 0 1

# 4 // 2 = 2



4 - 2 = 2
2! = 2



# if n = 5, then answer = 1 + 5 + 6 + 1 = 13

# 1 0 1 0 0
# 1 0 0 1 0
# 1 0 0 0 1
# 0 1 0 1 0
# 0 1 0 0 1
# 0 0 1 0 1

# 1 0 1 0 1


# 5 // 2 = 2
5 - 2 = 3
3! = 6

# 5 // 3 = 1

