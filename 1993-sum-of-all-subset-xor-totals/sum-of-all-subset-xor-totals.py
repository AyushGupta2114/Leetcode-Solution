from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])

        def xor_of_subset(subset):
            xor_result = 0
            for num in subset:
                xor_result ^= num
            return xor_result

        total_xor_sum = 0
        for subset in result:
            total_xor_sum += xor_of_subset(subset)
        
        return total_xor_sum

# Example usage
array = [1, 2, 3]
solution = Solution()
print(solution.subsetXORSum(array))  # Output will be the sum of XORs of all subsets

# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         def backtrack(start, path):
#             result.append(path[:])
#             for i in range(start, len(nums)):
#                 path.append(nums[i])
#                 backtrack(i + 1, path)
#                 path.pop()

#         result = []
#         backtrack(0, [])

#         def xor_of_subset(subset):
#             xor_result = 0
#             for num in subset:
#                 xor_result ^= num
#             return xor_result

#         def xor_of_all_subsets(nums):
#             subsets = subsetXORSum(self,nums)
#             for subset in subsets:
#                 print(f"Subset: {subset}, XOR: {xor_of_subset(subset)}")

# # Example usage
#         array = [1, 2, 3]
#         xor_of_all_subsets(array)
#         return 0
