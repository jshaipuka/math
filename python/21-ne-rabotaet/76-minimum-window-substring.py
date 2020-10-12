# net reshenija

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        min_s = ""
        min_s_count = 0
        
        start = 0
        left_pointer = 0
        right_pointer = 0
        
        not_found_letters = list(t)
        
        for letter, i in s:
            if letter in t:
                start = i
                left_pointer = i
                not_found_letters.remove(letter)
                break
        
        for i in range(start + 1, len(s)):
            if not_found_letters:
                if letter in not_found_letters:
                    right_pointer = i
                    not_found_letters.remove(letter)
        
        return min_s