class Solution:
    def findComplement(self, num: int) -> int:
    # Get the binary representation of the number without the '0b' prefix
        binary_rep = bin(num)[2:]
        a=[]
        for i in binary_rep:
            if(i=="1"):
                i=0
            else:
                i=1
            a.append(i)
        print(a)
        return int(''.join(map(str,a)),2)