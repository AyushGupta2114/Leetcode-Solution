from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        # Calculate prefix sum
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # Calculate suffix sum
        suffix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]

        result = []
        for i in range(n):
            left_sum = nums[i] * (i + 1) - prefix_sum[i]  # Absolute difference with elements on the left
            right_sum = suffix_sum[i] - nums[i] * (n - i)  # Absolute difference with elements on the right
            result.append(left_sum + right_sum)

        return result
