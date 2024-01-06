class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
	    return date(year, month, day).strftime("%A") 
# class Solution:
#     def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#         a=0
#         if (year % 400 == 0) and (year % 100 == 0):
#             a=366
#         elif (year % 4 ==0) and (year % 100 != 0):
#             a=366
#         else:
#             a=365
#         m=1
#         days=0
#         if a==366:
#             while(m<=month):
#                 if(m==2):
#                     days+=29
#                 elif(m==7):
#                     days+=31
#                 elif(m%2==0):
#                     days+=31
#                 else:
#                     days+=30
#                 m+=1
#         else:
#             while(m<=month):
#                 if(m==2):
#                     days+=28
#                 elif(m==7):
#                     days+=31
#                 elif(m%2==0):
#                     days+=30
#                 else:
#                     days+=31
#                 m+=1
#         print(days)
#         days+=day+1
#         bike=days%7
#         print(bike)
#         if bike == 0:
#             print("mon")

#         elif bike == 1:
#             print("tue")

#         elif bike == 2:
#             print("wed")

#         elif bike == 3:
#             print("thr")

#         elif bike == 4:
#             print("fri")
#         elif bike == 5:
#             print("sat")

#         elif bike == 6:
#             print("sum")


        