class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary_rep = bin(n)[2:]
        a=[]
        for i in binary_rep:
            if(i=="1"):
                i=0
            else:
                i=1
            a.append(i)
        print(a)
        return int(''.join(map(str,a)),2)
        