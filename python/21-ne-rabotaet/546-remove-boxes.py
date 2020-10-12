class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def solve(arr, pointer, score):
            if not arr or pointer <= 0:
                return score
            else:
                
                # delete color
                color = arr[pointer - 1]
                color_counter = 0
                new_pointer = -1
                

                for i in range(pointer - 1, -1, -1):
                    if arr[i] == color:
                        color_counter += 1
                    else:
                        new_pointer = i + 1
                        break
                
                new_score = score + color_counter * color_counter
                maximum = solve(arr[:new_pointer], new_pointer, new_score)
                
                # 131122231143111
                # 1311222311111
                first_time = True
                for i in range(new_pointer - 1, -1, -1):
                    if arr[i] == color:
                        if first_time:
                            first_time = False
                            united = solve(arr[:i + 1] + arr[new_pointer:], pointer - (new_pointer - 1 - i - 1 + 1), score)
                            deleted = solve(arr[i + 1:new_pointer], new_pointer - i - 1, 0)
                            
                            maximum = max(
                                maximum,
                                united + deleted
                            )
                    else:
                        first_time = True
                       
                return maximum
        
        return solve(boxes, len(boxes), 0)


# time limit not exceeded:
288 ms	18.7 MB
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        cache = dict()
        
        def solve(arr, pointer):
           # print("pointer", arr, pointer)
            
            if not arr or pointer <= 0:
                return 0
            elif arr in cache:
                return cache[arr]
            else:
                
                # delete color
                color = arr[pointer - 1]
                color_counter = 0
                new_pointer = -1
                

                for i in range(pointer - 1, -1, -1):
                    if arr[i] == color:
                        color_counter += 1
                    else:
                        new_pointer = i + 1
                        break
                
                
                maximum = color_counter * color_counter + solve(arr[:new_pointer], new_pointer)
                
                # 131122231143111
                # 1311222311111
                first_time = True
                for i in range(new_pointer - 1, -1, -1):
                    if arr[i] == color:
                        if first_time:
                            first_time = False
                            united = solve(arr[:i + 1] + arr[new_pointer:], pointer - (new_pointer - 1 - i - 1 + 1))
                            deleted = solve(arr[i + 1:new_pointer], new_pointer - i - 1)
                            
                            maximum = max(
                                maximum,
                                united + deleted
                            )
                    else:
                        first_time = True
                
                cache[arr] = maximum
                return maximum
        
        result = solve(tuple(boxes), len(boxes))
        #print("result", cache)
        return result
                
        