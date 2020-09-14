class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        sum = [0 for _ in range(n + 1)]
        for i in range(n):
            sum[i+1] = sum[i] + nums[i]
        self.sum = sum
    #         self.data = nums
    #         n = len(nums)
    #         self.cache = []

    #         for i in range(n):
    #             sum = 0
    #             for j in range(i, n):
    #                 sum = sum + nums[j]
    #                 self.cache.append((f'{i}{j}', sum))

    #         self.cache = dict(self.cache)


    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j + 1] - self.sum[i]
        # return self.cache[f'{i}{j}']
        # if i == j:
        #     return self.data[j]
        # # else:
        # return self.data[j] + self.sumRange(i, j - 1 )


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)