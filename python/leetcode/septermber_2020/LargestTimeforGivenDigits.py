from typing import List
from itertools import permutations


class Solution:

    #    min = 00:00, largest = 23:59

    def largestTimeFromDigits2(self, A: List[int]) -> str:
        # hours = filter(A, lambda a -> a < 4)

        # if more two numbers are >5. No solution exists
        # if more than 3 numbers are > 3. No solution exists

        # [0 - 2] [0 - 3] [0 - 5] [0 - 9]
        # if I break arr in 2: [0 - 2] [0 - 3] and rest
        # I am also interested in max numbers for those two

        hours_first = []
        hours_second = []
        minutes_first = []
        minutes_second = []

        for digit in A:
            if digit >= 0 and digit <= 2:
                hours_first.append(digit)
            elif digit >= 0 and digit <= 9:
                hours_second.append(digit)

        if len(hours_first) < 1:
            return ""

        print("hours_first", A, hours_first)
        hours_first.sort(reverse=True)
        hour_1 = hours_first.pop(0)
        print("hours_first", hours_first)

        hours_second = hours_second + hours_first
        if len(hours_second) < 1:
            return ""

        hours_second.sort(reverse=True)

        if hour_1 == 2:
            right_digits = list(filter(lambda digit: digit <= 3, hours_second))
            if not len(right_digits):
                return ""

            hour_2 = hours_second.pop(hours_second.index(right_digits[0]))
        else:
            hour_2 = hours_second.pop(0)

        for digit in hours_second:
            if digit >= 0 and digit <= 5:
                minutes_first.append(digit)
            elif digit >= 0 and digit <= 9:
                minutes_second.append(digit)

        if len(minutes_first) < 1:
            return ""

        minutes_first.sort(reverse=True)
        minutes_1 = minutes_first.pop(0)

        print(minutes_second)
        minutes_second = minutes_second + minutes_first
        print(minutes_second)
        if len(minutes_second) < 1:
            return ""
        minutes_second.sort(reverse=True)
        minutes_2 = minutes_second.pop(0)

        return '%s%s:%s%s' % (hour_1,hour_2,minutes_1,minutes_2)

    def compareClocks(self, best_clock: List[int], clock: List[int]):
        best_hours = best_clock[0] * 10 + best_clock[1]
        best_minutes = best_clock[2] * 10 + best_clock[1]
        hours = clock[0] * 10 + clock[1]
        minutes = clock[2] * 10 + clock[1]


    def largestTimeFromDigits(self, A: List[int]) -> str:
        clocks = list(filter(lambda clock: clock[:2] < (2, 4) and clock[2] < 6, permutations(A)))

        best_clock = ''

        for clock in clocks:
            if best_clock == '':
                best_clock = clock
            else:
                best_hours = best_clock[0] * 10 + best_clock[1]
                best_minutes = best_clock[2] * 10 + best_clock[1]
                hours = clock[0] * 10 + clock[1]
                minutes = clock[2] * 10 + clock[1]

                if hours > best_hours or (hours == best_hours and minutes > best_minutes):
                    best_clock = clock

        print(clocks)
        return '%s%s:%s%s' % best_clock if len(best_clock) else ''


print("============ [5,5,5,5] => '", Solution().largestTimeFromDigits([5,5,5,5]), "' Expected: ''")
print("============ [1,2,3,4] => '", Solution().largestTimeFromDigits([1,2,3,4]), "' Expected: 23:41")
print("============ [0,0,4,0] => '", Solution().largestTimeFromDigits([0,0,4,0]), "' Expected: 04:00")
print("============ [2,0,6,6] => '", Solution().largestTimeFromDigits([2,0,6,6]), "' Expected: 06:26")
print("============ [0,0,1,0] => '", Solution().largestTimeFromDigits([0,0,1,0]), "' Expected: 10:00")

#
# def largestTimeFromDigits(self, A: List[int]) -> str:
#     max_time = -1
#     # enumerate all possibilities, with the permutation() func
#     for h, i, j, k in itertools.permutations(A):
#         hour = h*10 + i
#         minute = j*10 + k
#         if hour < 24 and minute < 60:
#             max_time = max(max_time, hour * 60 + minute)
#
#     if max_time == -1:
#         return ""
#     else:
#         return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)