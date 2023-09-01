class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
        # for i in s:
        #     print(s[-1])
        #     k=s.remove(s[-1])
        #     s.insert(0,k)
        