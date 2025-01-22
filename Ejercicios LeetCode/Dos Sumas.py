class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

nums = [3, 4, 5, 6]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))  # Salida esperada: [1, 2]
