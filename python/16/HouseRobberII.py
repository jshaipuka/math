class Solution:
    def rob(self, nums: List[int]) -> int:



Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.


Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.


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
