class Solution:
    def findIntegers(self, num: int) -> int:
        def solve(num_str):
            print("num_str", num_str)
            if len(num_str) == 2:
                return 3
            elif len(num_str) == 1:
                return 1 if num_str == "1" else 0
            else:
            
                if num_str.startswith("11"):
                    # dont count it
                    return solve(num_str[1:])
                else:
                    return 1 + solve(num_str[2:])
                
        return solve("{0:b}".format(num))