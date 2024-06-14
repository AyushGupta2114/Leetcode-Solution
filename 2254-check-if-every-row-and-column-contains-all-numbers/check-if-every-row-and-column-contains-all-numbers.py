# please check carefully
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # Check rows
        for i in range(len(matrix)):
            row_values = sorted(matrix[i])
            if row_values != list(range(1, len(matrix) + 1)):
                return False

        # Check columns
        expected_set = set(range(1, len(matrix) + 1))
        for col in range(len(matrix[0])):
            column_values = set(matrix[row][col] for row in range(len(matrix)))
            if column_values != expected_set:
                return False

        return True

# from typing import List
# class Solution:
#     def checkValid(self, matrix: List[List[int]]) -> bool:
#         x=True
#         for i in range(0,len(matrix)):
#             print(matrix[i])
#             for j in range(0,len(matrix[i])):
#                 matrix[i].sort()
#                 # print(matrix[i][j],end=" ")
#                 if matrix[i][j]!=(j+1):
#                     x=False
#         print(x)

#         expected_set = set(range(1, len(matrix) + 1))
#         for col in range(len(matrix[0])):
#             column_values = set(matrix[row][col] for row in range(len(matrix)))
#             if column_values != expected_set:
#                 return False
#         # y=True
#         # expected_set = set(range(1,len(matrix)+1))
#         # # print(expected_set)
#         # for col in range(len(matrix[0])):
#         # # Collect all values in the current column
#         #     column_values = set(matrix[row][col] for row in range(len(matrix)))
#         #     print(column_values)
#         #     if column_values!=expected_set:
#         #         y=False
#         # print(y)
#         return True
#         # if x and y:
#         #     return True
#         # else:
#         #     return False


# # class Solution:
# #     def checkValid(self, matrix: List[List[int]]) -> bool:
# #         # Check rows
# #         for i in range(len(matrix)):
# #             row_values = sorted(matrix[i])
# #             if row_values != list(range(1, len(matrix) + 1)):
# #                 return False

# #         # Check columns
# #         expected_set = set(range(1, len(matrix) + 1))
# #         for col in range(len(matrix[0])):
# #             column_values = set(matrix[row][col] for row in range(len(matrix)))
# #             if column_values != expected_set:
# #                 return False

# #         return True

