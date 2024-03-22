#include <algorithm>
class Solution {
public:
    bool isPalindrome(ListNode* head)
    {
        
        struct ListNode *q=head;
        struct ListNode *p=head;
        int a=0,i=0;
        while(q!=NULL)
        {
            a++;
            q=q->next;
        }
        printf("%d",a);
        int array[a];
        while(p!=NULL)
        {
            array[i]=p->val;
            p=p->next;
            i++;

        } 
        int arr2[a],k=0;
        copy(array, array+a, arr2);
        int temp, j;  
        for ( i = 0, j = a - 1; i < a/2; i++, j--)  
        {     
            temp = array[i];  
            array[i] = array[j];  
            array[j] = temp;  
        }   
        // use for loop to print the reverse array  
        for ( i = 0; i < a; i++)  
        {  
            if(array[i]==arr2[i])
                k++;
            else
                return false;
        }
        return true;
 }
};