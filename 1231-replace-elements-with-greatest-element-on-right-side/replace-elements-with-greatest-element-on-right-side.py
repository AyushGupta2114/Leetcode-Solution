class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        #copied
        # Traverse the list from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Store the current element
            current = arr[i]
            # Replace the current element with the maximum value to its right
            arr[i] = max_right
            # Update the maximum value to the right
            max_right = max(max_right, current)
        
        return arr




        # # for i in range(len(arr)-1):
        # #     for j in range(i+1,arr):
        # #         print(arr[i],arr[j])
        # for i in range(len(arr)-1):
        #     maxy=arr[i]
        #     print(arr[i])
        #     for j in range(i+1,len(arr)-1):
        #         if(arr[j+1]>maxy):
        #             arr[j]=maxy
        #     arr[i]=maxy
        # return arr

        