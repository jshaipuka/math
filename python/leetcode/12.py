from typing import List

class Solution:

    # 00 01 10 11
    # m = 0, n = 1
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def checkStr(str, count_zeroes, count_ones):
            temp_count_zeroes = 0
            temp_count_ones = 0

            for si in str:
                if si == "0" and count_zeroes < m:
                    temp_count_zeroes += 1
                elif si == "1" and count_ones < n:
                    temp_count_ones += 1



            return temp_count_zeroes, temp_count_ones

        def solve(count_zeroes, count_ones, count_strs, str_index):
            if count_zeroes >= m or count_ones >= n or str_index == len(strs):
                return count_strs
            else:

                temp_count_zeroes, temp_count_ones = checkStr(strs[str_index], count_zeroes, count_ones)



                if temp_count_zeroes + count_zeroes < m or temp_count_ones + count_ones < n:
                    count_strs += 1

                    return max(
                        solve(count_zeroes + temp_count_zeroes, count_ones + temp_count_ones, count_strs, str_index + 1),
                        solve(count_zeroes + temp_count_zeroes, count_ones + temp_count_ones, count_strs, str_index + 2)
                    )


                return max(
                    solve(count_zeroes, count_ones, count_strs, str_index + 1),
                    solve(count_zeroes, count_ones, count_strs, str_index + 2)
                )


        return solve(0, 0, 0, 0)

print("============ '", Solution().findMaxForm(["10","0001","111001","1","0"], 5, 3), "' Expected: ''", 4)
