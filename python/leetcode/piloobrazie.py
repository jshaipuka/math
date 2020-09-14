#

# Задача №3002. Пилообразные последовательности - 210101010101010101010
#
# Назовем последовательность пилообразной, если каждый ее элемент либо строго больше, либо строго меньше своих соседей. По данными числам n и k определите число пилообразных последовательностей длины n, составленных из чисел 1..k.
# Входные данные
#
# Программа получает на вход два натуральных числа n и k,  1≤n≤1000, 1≤k≤1000.
# Выходные данные
#
# Необходимо вывести остаток от деления количества искомых последовательностей на 109+7.

def solve(n, k):
    print(n, k)
    if n == 0 or k == 0 or (n > 1 and k == 1):
        return 0
    elif n == 1 and k > 1:
        return k



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        cache = [-1]*n

        for i in range(n - 1, -1, -1):
            current = n - 1
            next = n - 2

            if cache[i] != -1:
                return cache[i]
            else:


        #         def solve(i):
        #             if i == n:
        #                 return 0
        #             if cache[i] != -1:
        #                 return cache[i]
        #             if i == n - 1:
        #                 return cost[n - 1]

        #             cache[i] = cost[i] + min(solve(i + 1), solve(i + 2))
        #             return cache[i]

        return min(solve(0), solve(1))

# n = len of saw sequence
# 1 ... k = numbers of saw sequence
def solve(n, k):
    print('solving')

    sequences = []

    210
    212

    def count_sequences(running_count, sequence, shouldGoUp):
        if shouldGoUp:

        last_sequence_element = sequence[-1] if len(sequence) > 0 else ""
        previous_sequence_element = sequence[-2] if len(sequence) > 1 else ""

        if last_sequence_element

        return running_count

    return count_sequences(0) % 109 + 7


print("============ '", solve(3, 3), "' Expected: ''", 10)
print("============ '", solve(30, 3), "' Expected: ''", 4356618)

