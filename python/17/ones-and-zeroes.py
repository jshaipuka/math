from collections import defaultdict
from typing import List

class Solution:

    # 00 01 10 11
    # m = 0, n = 1
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = defaultdict(int)
        out_of_bounds = len(strs)

        def solve(i, count_zeroes, count_ones):
            if i >= out_of_bounds:
                return 0
            elif (i, count_zeroes, count_ones) in cache:
                return cache[(i, count_zeroes, count_ones)]
            else:
                s = strs[i]
                next = i + 1
                ones = s.count('1')
                zeroes = s.count('0')

                take_string = solve(next, count_zeroes - zeroes, count_ones - ones) + 1 if zeroes <= count_zeroes and ones <= count_ones else 0
                dont_take_string = solve(next, count_zeroes, count_ones)

                result = max(dont_take_string, take_string)
                cache[(i, count_zeroes, count_ones)] = result
                return cache[(i, count_zeroes, count_ones)]

        return solve(0, m, n)


print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3), "' Expected: ''", 4)
print("============ '", Solution().findMaxForm(["10","0","1"], 1, 1), "' Expected: ''", 2)
print("============ '", Solution().findMaxForm(["00", "01", "10", "11"], 2, 2), "' Expected: ''", 2)
print("============ '", Solution().findMaxForm(["111","1000","1000","1000"], 9, 3), "' Expected: ''", 3)
print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 50, 50), "' Expected: ''", 5)


arr =["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
arr_m = 9
arr_n = 80

print("============ '", Solution().findMaxForm(arr, arr_m, arr_n), "' Expected: ''", "to not time out")
