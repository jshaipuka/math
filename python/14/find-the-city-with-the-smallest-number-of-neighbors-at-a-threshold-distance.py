# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
from math import inf

class Solution:
    def floydWarshall(self, n, edges):
        matrix = [ [inf]*n for i in range(n)]

        for k in range(n):
            for edge in edges:
                [i, j, weight] = edge

                old_path = matrix[i][j]
                new_path = matrix[k][j] + matrix[i][k]
                if new_path < old_path:
                    matrix[i][j] = new_path
                    matrix[j][i] = new_path
                elif new_path == inf:
                    matrix[i][j] = weight
                    matrix[j][i] = weight
        return matrix
    
    def findSmallestCityPath(self, matrix, distanceThreshold):
        answer_city = -1
        smallest_city_paths = inf
        
        for city in range(len(matrix)):    
            city_paths_count = len(list(filter(lambda path: path <= distanceThreshold, matrix[city])))

            if city_paths_count >= 0 and city_paths_count <= smallest_city_paths:
                answer_city = city
                smallest_city_paths = city_paths_count
            print("From", city, " can travel to ", city_paths_count, "cities. Current winner is", answer_city, "with only", smallest_city_paths, " neighbours")
        return answer_city
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = Solution.floydWarshall(self, n, edges)
        print(matrix)
        return Solution.findSmallestCityPath(self, matrix, distanceThreshold) 

        