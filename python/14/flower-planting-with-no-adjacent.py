# https://leetcode.com/problems/flower-planting-with-no-adjacent

# Pochti rabotaet
# Input
# 5
# [[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]]
# Output
# [1,4,1,2,3]
# Expected
# [1,1,2,3,2]

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        planted = [0 for garden in range(N)]
        flowers = [1,2,3,4]
        flower_index = 0

        for path in paths:
                [garden_from, garden_to] = path

                if planted[garden_from - 1] == 0:
                    planted[garden_from - 1] = flowers[flower_index]
                    flower_index = flower_index + 1 if flower_index + 1 < 4 else 0
                if planted[garden_to - 1] == 0:
                    planted[garden_to - 1] = flowers[flower_index]
                    flower_index = flower_index + 1 if flower_index + 1 < 4 else 0
        
        for i in range(len(planted)):
            if planted[i] == 0:
                planted[i] = 1
        
        return planted