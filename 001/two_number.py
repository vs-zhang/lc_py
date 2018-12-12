class Solution(object):
    def two_sum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target-n], i]
            d[n] = i


s = Solution()
result = s.two_sum([2,3,4], 7)
print(result)
