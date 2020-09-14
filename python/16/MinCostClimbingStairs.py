from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def solve(sum, i):
            if i == n - 1:
                return min(sum, solve(sum + cost[i], i + 1))
            elif i >= n:
                return sum
            else:
                return min(solve(sum + cost[i], i + 1), solve(sum + cost[i + 1], i + 2))

        return solve(0, 0)



print("cost = [10, 15, 20], answer ", Solution().minCostClimbingStairs([10, 15, 20])) # 15
print("cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], answer ", Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # 6

# Time limit exceeded

