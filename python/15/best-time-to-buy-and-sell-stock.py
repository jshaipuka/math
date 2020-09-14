class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0] if len(prices) else 0
        difference = 0

        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]

            new_difference = prices[i] - minimum

            if new_difference > difference:
                difference = new_difference

        return difference


    #
    #
    # class Solution:
    #     def isSubsequence(self, s: str, t: str) -> bool:
    #         it = iter(t)
    #         return all(c in it for c in s)



    #
    class Solution:
        saved = []

    def solve(self, nums):
        if len(nums) == 0:
            return 0
        if self.saved[len(nums) - 1] != -1:
            return self.saved[len(nums) - 1]
        if len(nums) == 1:
            return nums[0]

        self.saved[len(nums) - 1] = max(
            self.solve(nums[2::]) + nums[0],
            self.solve(nums[3::]) + nums[1]
        )
        return self.saved[len(nums) - 1]

    def rob(self, nums: List[int]) -> int:
        self.saved = [-1]*len(nums)
        return self.solve(nums)



    # class Solution:
    #     def rob(self, nums: List[int]) -> int:
    #
    #         c=0
    #         dc=0
    #         for i in range(len(nums)):
    #             temp=dc
    #             dc=max(c,dc)
    #             c=temp+nums[i]
    #         return max(c,dc)


    class Solution:
        def rob(self, nums: List[int]) -> int:
            p = 0
            q = 0
            for n in nums:
                t = p
                p = max(q + n, p)
                q = t
            return p




sample 24 ms submission

class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0

        dp = ["*"] * len(nums)


        for i in range(len(nums)):
            if (i == 0):
                dp[i] = nums[i]
            elif (i == 1):
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])



        return dp[-1]

