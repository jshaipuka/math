from collections import defaultdict

class Solution:

    # Runtime: 1792 ms, faster than 5.21% of Python3 online submissions for Can I Win.
    # Memory Usage: 87.9 MB, less than 5.04% of Python3 online submissions for Can I Win.
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        integers_pool = [i + 1 for i in range(maxChoosableInteger)]

        cache = defaultdict(bool)

        if maxChoosableInteger >= desiredTotal:
            return True
        elif maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        def solve(integers_left, running_total, player1_turn):
            if running_total >= desiredTotal:
                return not player1_turn
            elif not len(integers_left):
                return player1_turn
            elif (frozenset(integers_left), running_total, player1_turn) in cache:
                return cache[(frozenset(integers_left), running_total, player1_turn)]
            else:
                key = (frozenset(integers_left), running_total, player1_turn)
                for i in range(len(integers_left)):
                    int_array = integers_left[:i] + integers_left[i+1:]
                    r1 = solve(int_array, running_total + integers_left[i], not player1_turn)

                    if player1_turn and r1:
                        cache[key] = True
                        return True
                    if not player1_turn and not r1:
                        cache[key] = False
                        return False

                cache[key] = not player1_turn
                return not player1_turn
        return solve(integers_pool, 0, True)


# 4 3 lost
# 4 1 2 win
# 1 4 2|3 win

# 10+9+8+7+6+5+4+1 | win
# 10+1+9+2+8+3+7+4+6 | lose



print("============ '", Solution().canIWin(10, 11), "' Expected: ''", False)
print("============ '", Solution().canIWin(10, 0), "' Expected: ''", True)
print("============ '", Solution().canIWin(10, 1), "' Expected: ''", True)
print("============ '", Solution().canIWin(10, 40), "' Expected: ''", False)
print("============ '", Solution().canIWin(4, 6), "' Expected: ''", True)
