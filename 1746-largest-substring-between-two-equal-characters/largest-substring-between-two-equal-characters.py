
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

# Dictionary to store the first and last appearance of each character
        appearances = {}

# Variable to store the maximum distance
        max1 = -1

        for i, char in enumerate(s):
            if char not in appearances:
                # If the character is not in the dictionary, store its first appearance
                appearances[char] = {"first": i, "last": i}
            else:
                # If the character is already in the dictionary, update its last appearance
                appearances[char]["last"] = i
                # Update the maximum distance if needed
                max1 = max(max1, appearances[char]["last"] - appearances[char]["first"])

        # Print the maximum distance
        print("Maximum distance between first and last appearances:", max1)
        if(max1==-1):
            return -1
        return max1-1
        # old method 
        # max=-1
        # a=[]
        # for i in range(0,len(s)):
        #     if s[i] not in a:
        #         a.append(s[i])
        #     else:
        #         fi = s.index(s[i])
        #         se = s.index(s[i], fi + 1)

        #         if(se-fi)>max:
        #             max=se-fi
        # if(max==-1):
        #     return -1
        # return max-1

        # class Solution:
#     def maxLengthBetweenEqualCharacters(self, s: str) -> int:

#         # appearances = {}
#         # max1 = -1
#         # for i, char in enumerate(s):
#         #     if char not in appearances:
#         #         appearances[char] = {"first": i, "last": i}
#         #     else:
#         #         appearances[char]["last"] = i
#         #         max1 = max(max1, appearances[char]["last"] - appearances[char]["first"])

#         # print("Maximum distance between first and last appearances:", max1)
#         # if(max1==-1):
#         #     return -1
#         # return max1-1
#         # old method 
#         max1=-1
#         a=[]
#         for i in range(0,len(s)):
#             if s[i] not in a:
#                 a.append(s[i])
#             else:
#                 fi = s.index(s[i])
#                 se = s.index(s[i], fi + 1)

#                 if(se-fi)>max1:
#                     max1=se-fi
#                 print(se,fi)
#         if(max1==-1):
#             return -1
#         return max1-1

        