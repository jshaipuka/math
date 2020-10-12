class Solution:

    #40 ms	14.1 MB
    def firstMissingPositive(self, nums: List[int]) -> int:
       # positives = [ i + 1 for i in range(len(nums)) ]
        positives = []
        
        for i in range(len(nums)):
            num = i + 1
            if num not in nums:
                positives.append(num)

        return positives[0] if positives else len(nums) + 1