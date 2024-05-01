class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=word.find(ch)
        b=word[0:a+1]
        c=word[a+1::]
        print(b,c)
        return b[::-1]+c

        
        