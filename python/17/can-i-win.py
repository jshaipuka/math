class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        integers_pool = [i + 1 for i in range(maxChoosableInteger)]

        cache = dict()


        if maxChoosableInteger >= desiredTotal:
            return True

        def solve(integers_left, running_total, player1_turn):
            # print("integers_left, running_total, player1_turn", integers_left, running_total, player1_turn)
            # print("sum(integers_left) < desiredTotal", sum(integers_left),  desiredTotal, sum(integers_left) < desiredTotal)
            # if sum(integers_left) < desiredTotal:
            #
            #     return False
            if running_total >= desiredTotal or sum(integers_left) + running_total < desiredTotal:
                return not player1_turn
            else:
                return (
                    solve(integers_left[1:], running_total + integers_left.pop(), not player1_turn)
                    or
                    solve(integers_left[:-1], running_total + integers_left[-1], not player1_turn)
                )
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
