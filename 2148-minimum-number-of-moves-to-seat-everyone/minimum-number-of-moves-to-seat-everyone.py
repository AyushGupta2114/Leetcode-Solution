class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        k=0
        seats.sort()
        students.sort()
        for i in range(0,len(seats)) :
            k+=abs(seats[i]-students[i])
        return k 
        