/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    
    struct ListNode *cur=head;
    struct ListNode *fwd=head,*newList=NULL;
    while(cur!=NULL)
    {
        fwd=cur->next;
        cur->next=newList;
        newList=cur;
        cur=fwd;
    }
    return newList;
    

}