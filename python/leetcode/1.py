from typing import List

class Solution:

    # 00 01 10 11
    # m = 0, n = 1
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=len)

        cache = []

        def checkStr(str, count_zeroes, count_ones, count_strs):
            temp_count_zeroes = 0
            temp_count_ones = 0

            for si in str:
                if si == "0":
                    temp_count_zeroes += 1
                elif si == "1":
                    temp_count_ones += 1

            sum_count_zeroes = temp_count_zeroes + count_zeroes
            sum_count_ones = temp_count_ones + count_ones

            if sum_count_zeroes <= m and sum_count_ones <= n:
                return sum_count_zeroes, sum_count_ones, count_strs + 1

            return count_zeroes, count_ones, count_strs

        def solve(count_zeroes, count_ones, count_strs, str_index):
            print(count_zeroes, count_ones, count_strs, str_index, strs[str_index] if str_index < len(strs) else "out of range")

            if str_index >= len(strs) or (count_zeroes >= m and count_ones >= n):
                return count_strs if count_strs <= len(strs) else len(strs)
            else:
                new_count_zeroes, new_count_ones, new_count_strs = checkStr(strs[str_index], count_zeroes, count_ones, count_strs)

                return max(
                    new_count_strs,
                    solve(new_count_zeroes, new_count_ones, new_count_strs, str_index + 1),
                    solve( count_ones, count_strs, count_strs, str_index + 1)
                )


        return solve(0, 0, 0, 0)

print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3), "' Expected: ''", 4)
print("============ '", Solution().findMaxForm(["10","0","1"], 1, 1), "' Expected: ''", 2)
print("============ '", Solution().findMaxForm(["00", "01", "10", "11"], 2, 2), "' Expected: ''", 2)
print("============ '", Solution().findMaxForm(["111","1000","1000","1000"], 9, 3), "' Expected: ''", 3)
print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 50, 50), "' Expected: ''", 5)
