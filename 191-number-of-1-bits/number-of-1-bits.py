class Solution:
    def hammingWeight(self, n: int) -> int:
        print(bin(n))
        return Counter(bin(n))["1"]

            
        