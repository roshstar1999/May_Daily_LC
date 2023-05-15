class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        x=head
        length=0
        knode=None
        while x:

            length+=1
            
            if k==length:
                knode=x
            x=x.next
        
        countt=0
        x=head
        while x:
            countt+=1
            if length-k+1==countt:
                
                knode.val,x.val=x.val,knode.val
                return head
            x=x.next
