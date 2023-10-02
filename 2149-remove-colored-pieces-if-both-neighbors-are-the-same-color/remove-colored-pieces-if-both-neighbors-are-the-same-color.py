class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice=0
        bob=0
        for i in range(1,len(colors)-1):
            if(colors[i-1]==colors[i+1] and colors[i-1]==colors[i]):
                if(colors[i]=='A'):
                    alice+=1
                else:
                    bob+=1
        if(alice>bob):
            return True 
        else:
            return False