# Runtime: 64 ms
# Memory Usage: 13.9 MB

# Improvement
# Where to start? The biggest problem of the code above is that there are too many cases. What if we can combine them? Notice that the biggest difference between case 2 and case 3 is the condition of the first char.
# By combining case 2 and case 3, we get a new pattern: No matter what first char is, the rest should be lowercase.
# https://leetcode.com/articles/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) > 1:
            first = word[0] == word[0].upper()
            second = word[1] == word[1].upper()

            if not first and second:
                return False

            for letter_i in range(2, len(word)):
                both_upper = second and word[letter_i] == word[letter_i].upper()
                both_lower = not second and word[letter_i] != word[letter_i].upper()

                if not both_upper and not both_lower: return False

            return True
        else:
            return True

















# sample 36 ms submission
def detectCapitalUse(self, word: str) -> bool:
    if word.islower() or word.isupper():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    return False


# sample 24 ms submission
def detectCapitalUse(self, word: str) -> bool:
    if word.lower() == word: return True
    elif word.upper() == word: return True
    elif word.istitle(): return True
    else: return False

# sample 12 ms submission
def detectCapitalUse(self, word: str) -> bool:
    if(word.lower()==word):
        return True
    if(word.upper()==word):
        return True
    if(word[0].upper()==word[0] and word[1:].lower()==word[1:]):
        return True
    return False

# sample 16 ms submission
def detectCapitalUse(self, word: str) -> bool:
    if len(word) <= 1:
        return True
    cap1 = word[1]
    for c in word[2:]:
        if c.islower() != cap1.islower():
            return False
    if word[0].islower() and cap1.isupper():
        return False
    return True


# sample 13564 kb submission
def detectCapitalUse(self, str):
    if str.islower() or str.isupper() or str.istitle():
      return True
    else:
      return False


