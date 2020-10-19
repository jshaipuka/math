class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        
        not_found = list(t)
        counter = dict()
        
        min_window_s = (len(s), "")
        
        for letter in not_found: 
            counter[letter] = 0

        for right in range(len(s)):
            if len(not_found) == 0: # right_stop_condition
                stop = False
                while left <= right or not stop: # within_bounds_condition
                    letter = s[left]
                    if letter in counter:
                        counter[letter] -= 1
                        new_distance = right - left
                        min_window_s = (new_distance, s[left:right]) if not len(not_found) and new_distance < min_window_s[0] else min_window_s

                        if counter[letter] == 0:
                            not_found.append(letter) # exit_condition
                            stop = True

                    left += 1

                        
            # remove letter and/or update counter
            letter = s[right]
            if letter in counter:
                counter[letter] += 1
                if letter in not_found:
                    not_found.remove(letter)
         
        print(min_window_s)
        return min_window_s[1]