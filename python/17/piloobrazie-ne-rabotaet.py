# Задача №3002. Пилообразные последовательности - 210101010101010101010
#
# Назовем последовательность пилообразной, если каждый ее элемент либо строго больше, либо строго меньше своих соседей. По данными числам n и k определите число пилообразных последовательностей длины n, составленных из чисел 1..k.
# Входные данные
#
# Программа получает на вход два натуральных числа n и k,  1≤n≤1000, 1≤k≤1000.
# Выходные данные
#
# Необходимо вывести остаток от деления количества искомых последовательностей на 10**9+7.


# n = 3, k = 3, answer = 10
# n = 30, k = 3, answer = 4356618


# n = длина пилообразных последовательностей
# k = числа, которые входят в последовательность
def solve(n, k):
    def mySolution(n, k, last_2ints):
        if n == 0 or k == 0 or (n > 1 and k == 1):
            return 0
        elif n == 1 and k > 1:
            return k
        else:
            digit1, digit2 = last_2ints

            if digit1 > digit2:
                solve_with_less_k = mySolution(n, k - 1, (digit1, digit2 - 1))
                solve_with_less_n = mySolution(n - 1, k, (digit1 + 1, digit2))
                return solve_with_less_n + solve_with_less_k
            elif digit1 < digit2:
                solve_with_less_k = mySolution(n, k - 1, (digit1, digit2 + 1))
                solve_with_less_n = mySolution(n - 1, k, (digit1 - 1, digit2))
                return solve_with_less_n + solve_with_less_k

            return mySolution(n, k, (digit1, digit2 - 1))
    return mySolution(n, k, (-1,-1))

# k,n = 0
# Always 0
print("n = 0, k = 2, answer ", solve(0, 2)) # 0
print("n = 6, k = 0, answer ", solve(6, 0)) # 0

# n > 1, k = 1
# always 0
print("n = 2, k = 1, answer ", solve(2, 1)) # 0

# n = 1, k > 1
# always k
print("n = 1, k = 2, answer ", solve(2, 1)) # 1

print("n = 2, k = 2, answer ", solve(2, 2)) #2
print("n = 2, k = 3, answer ", solve(2, 3)) #
print("n = 2, k = 4, answer ", solve(2, 4)) #12
print("n = 3, k = 3, answer ", solve(3, 3)) # 10
