import math
class Solution:
    def isPalindrome(self, x):
        temp=str(x)
        return (temp==temp[::-1])
            # retu