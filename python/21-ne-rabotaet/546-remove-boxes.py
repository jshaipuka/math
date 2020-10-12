class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def solve(arr, pointer, score):
            print("arr", arr, pointer)
            if not arr or pointer < 0:
                print("score", score)
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
                        new_pointer = i
                        break;
                
                new_score = score + color_counter * color_counter
                print("new_score", color, score, color_counter, new_score)
                    
                return max(
                    solve(arr, pointer - 1, score),
                    1 + solve(arr[:new_pointer], new_pointer, new_score)
                )
        
        return solve(boxes, len(boxes), 0)
                
        