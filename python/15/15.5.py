# Разбиения на k слагаемых
# Для данных натуральных чисел n и k определите количество способов представить число n в виде суммы k натуральных слагаемых, если способы, отличающиеся только порядком слагаемых считать одинаковыми.

# Входные данные
# Программа получает на вход два натуральных числа n и k, не превосходящих 150. Гарантируется, что ответ не превосходит 231-1.

# Выходные данные
# Выведите ответ на задачу.

# Примечание
# Эту задачу разрешается (и рекомендуется) решать, при помощи Memorization.


# ====================================
def solve(n, k):
    print(n, k)
    if n == 0 or k == 0 or n < k:
        return 0
    elif k == 1 or k == n:
        return 1
    elif n > k:
        return solve(n - k, k) + solve(n - 1, k - 1)
        # return solve(n, k - 1) + solve(n - k, k)

print("n = 6, k = 3, answer ", solve(6, 3)) # 3

# k,n = 0
# Always 0
print("n = 0, k = 2, answer ", solve(0, 2)) # 0
print("n = 6, k = 0, answer ", solve(6, 0)) # 0


# n != 0, k = 1
# always 1
print("n = 2, k = 1, answer ", solve(2, 1)) # 1 2 = 2

# n == k
# always 1
print("n = 2, k = 2, answer ", solve(2, 2)) # 2 = 1 + 1

# n < k
# always 0
print("n = 3, k = 5, answer ", solve(3, 5)) # 0
# 3 = 1 + 1 + 1 + 0 + 0

# n > k
print("n = 3, k = 2, answer ", solve(3, 2))
# 3 = 1 + 2 = (2 + 1)
# 1 way
print("n = 5, k = 2, answer ", solve(5, 2))
# 5 = 1 + 4 = 2 + 3 = (3 + 2) = (4 + 1)
# 2 ways


print("n = 5, k = 3, answer ", solve(5, 3))
# 5 = 1 + 1 + 3 = 1 + 2 + 2
# 2 ways


print("n = 8, k = 3, answer ", solve(8, 3))
# 8 = 1 + 1 + 6 = 1 + 2 + 5 = 1 + 3 + 4 = (1 + 5 + 2) = (1 + 6 + 1) = !1 + 7 + 0
#   = (2 + 1 + 5) = 2 + 2 + 4 = 2 + 3 + 3 = (2 + 4 + 2) = (2 + 5 + 1) = !2 + 6 + 0
#   = (3 + 1 + 4) = ....
#
#
# 5 = solve 5, 1 + solve 5 - 2, 2 = 1 + solve 3, 2 = 1 + solve 3, 1 + solve 1, 2= 1 + 1 + 0
#
# solve 5, 1 = 1

