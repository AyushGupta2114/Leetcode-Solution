class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_of_10 = 0
        num_of_5 = 0
        # num_of_20 = 0
        shopper = 0
        for i in bills:
            if i == 5:
                num_of_5 += 1
                shopper += i
            elif i == 10:
                num_of_10 += 1
                shopper += i - 5
                if num_of_5 >= 1:
                    num_of_5 -= 1
                    continue
                else:
                    return False
            else:
                shopper += 20
                if num_of_10 >= 1 and num_of_5 >= 1:
                    num_of_10 -= 1
                    num_of_5 -= 1
                elif num_of_5 >= 3:
                    num_of_5 -= 3
                else:
                    return False
        return True

        # shopper=0
        # for i in bills:
        #     if(i==5):
        #         shopper+=i
        #         print(shopper)
        #     elif(i>5):
        #         shopper+=i
        #         shopper-=5
        #         print(shopper)
        #         if(shopper<0):
        #             return False
        # return True
