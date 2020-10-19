class Solution:
    def findIntegers(self, num: int) -> int:
        cache = dict()
        
        def solve(num_str, start):
            if num_str in cache:
                return cache[num_str]
            elif len(num_str) == 1:
                return 2
            else:
                count = 0
                print(num_str, start)
                
                for i in range(start + 1, len(num_str)):
                    digit = num_str[i]
                    if digit == "1":
                        smaller_length_number = num_str[:i] + "0" + num_str[i + 1:]
                        same_length_number = num_str[:i] + "10" + num_str[i + 2:] if len(num_str[i + 2:]) >= 2 else num_str[:i]
                        
                        count1 = solve(smaller_length_number, i)
                        count2 = solve(same_length_number, i)
                        count += count1 + count2
                        
                count3 = solve(num_str[:-1], 0)
                count += count3
                cache[num_str] = count
                
        return solve("{0:b}".format(num), 0)