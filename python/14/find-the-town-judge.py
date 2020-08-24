# https://leetcode.com/problems/find-the-town-judge
# Rabotaet

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # index = person -1
        # (0, 0) = (trusted_by, trusts_others)
        counter = [(0, 0) for _ in range(N)]
        
        for trust_relationship in trust:
            [a, b] = trust_relationship
            
            [ai, bi] = [a - 1, b - 1] # correct indexes of a and b
            counter[ai] = (counter[ai][0], counter[ai][1] + 1)
            counter[bi] = (counter[bi][0] + 1, counter[bi][1])
        
        judge = counter.index((N - 1, 0)) + 1 if (N - 1, 0) in counter else -1
        
        return judge