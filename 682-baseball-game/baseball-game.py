class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        # if len(operations)==1:
        #     return operation[0]
        for i in operations:
            if i=="C":
                score.pop()
            elif(i=="D"):
                score.append(score[-1]*2)
            elif(i=="+"):
                score.append(int(score[-1])+int(score[-2]))
            else:
                score.append(int(i))
            print(score)
        return sum(score)


        