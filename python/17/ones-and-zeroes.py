from typing import List

class Solution:

    # 00 01 10 11
    # m = 0, n = 1
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs.sort(key=len)

        cache = [dict() for i in range(len(strs))]

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
            # print(count_zeroes, count_ones, count_strs, str_index, strs[str_index] if str_index < len(strs) else "out of range")

            if str_index >= len(strs) or (count_zeroes >= m and count_ones >= n):
                return count_strs if count_strs <= len(strs) else len(strs)
            else:
                key = "%s%s" % (count_zeroes, count_ones)
                if key in cache[str_index]:
                    return cache[str_index][key]
                else:
                    cache[str_index][key] = count_strs

                    new_count_zeroes, new_count_ones, new_count_strs = checkStr(strs[str_index], count_zeroes, count_ones, count_strs)

                    new_key = "%s%s" % (new_count_zeroes, new_count_ones)
                    cache[str_index][new_key] = new_count_strs

                    return max(
                        # new_count_strs,
                        solve(new_count_zeroes, new_count_ones, new_count_strs, str_index + 1),
                        solve( count_ones, count_strs, count_strs, str_index + 1)
                    )

        return solve(0, 0, 0, 0)

print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3), "' Expected: ''", 4)
print("============ '", Solution().findMaxForm(["10","0","1"], 1, 1), "' Expected: ''", 2)
print("============ '", Solution().findMaxForm(["00", "01", "10", "11"], 2, 2), "' Expected: ''", 2)
print("============ '", Solution().findMaxForm(["111","1000","1000","1000"], 9, 3), "' Expected: ''", 3)
print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 50, 50), "' Expected: ''", 5)


arr =["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
arr_m = 9
arr_n = 80

print("============ '", Solution().findMaxForm(arr, arr_m, arr_n), "' Expected: ''", "to not time out")
