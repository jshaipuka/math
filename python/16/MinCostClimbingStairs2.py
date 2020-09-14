from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1 for _ in range(n)]

        def solve(sum, i):
            if i < n and cache[i] >= 0:
                return cache[i]
            else:
                if i == n - 1:
                    res = min(sum, solve(sum + cost[i], i + 1))
                    cache[i] = res
                    return res
                elif i >= n:
                    # cache[i] = sum
                    return sum
                else:
                    res = min(solve(sum + cost[i], i + 1), solve(sum + cost[i + 1], i + 2))
                    cache[i] = res
                    return res

        return solve(0, 0)



print("cost = [10, 15, 20], answer ", Solution().minCostClimbingStairs([10, 15, 20])) # 15
print("cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], answer ", Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # 6

# Time limit exceeded

#
# F (n) =
# n in Fcache:  Fcache[n]
# n = 0:  0, and cache it as Fcache[0]
# n = 1:  1, and cache it as Fcache[1]
# else:  F (n - 2) + F (n - 1), and cache it as Fcache[n]


# if x is in cache:
#     return cache[x]
# else:
#     res <- .. do something with f(x-k)
#         cahce[x] <- res
#     return res
