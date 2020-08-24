class Solution:
    
    def remove(self, arr, a):
        if a in arr:
            arr.remove(a)
        
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        planted = [0 for garden in range(N)]
        colored = [[1,2,3,4] for garden in range(N)]

        for path in paths:
                [garden_from, garden_to] = path
                
                if planted[garden_from - 1] == 0 and planted[garden_to - 1] == 0:
                    # init
                    planted[garden_from - 1] = 1
                    planted[garden_to - 1] = 2
                    colored[garden_from - 1].remove(2)
                    colored[garden_to - 1].remove(1)
                    
                elif planted[garden_from - 1] == 0 and planted[garden_to - 1] != 0:
                    self.remove(colored[garden_from - 1], planted[garden_to - 1])
                    planted[garden_from - 1] = colored[garden_from - 1][0]
                    self.remove(colored[garden_to - 1], planted[garden_from - 1])
                elif planted[garden_from - 1] != 0 and planted[garden_to - 1] == 0:
                    self.remove(colored[garden_to - 1], planted[garden_from - 1])
                    planted[garden_to - 1] = colored[garden_to - 1][0]
                    self.remove(colored[garden_from - 1], planted[garden_to - 1])
                elif planted[garden_from - 1] != 0 and planted[garden_to - 1] != 0 and planted[garden_from - 1] == planted[garden_to - 1]:
                    # same flower in both gardens
                    self.remove(colored[garden_from - 1], planted[garden_to - 1])
                    planted[garden_from - 1] = colored[garden_from - 1][0]
                    
                    

        for i in range(len(planted)):
            if planted[i] == 0:
                planted[i] = 1
        
        return planted
                    
            