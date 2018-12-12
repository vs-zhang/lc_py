from helper.ListNode import ListNode
from helper.SingleLinkedList import SingleLinkedList

class Solution(object):
    def add_two_number(self, l1, l2):
        p = dummy = ListNode(-1)
        carry = 0
        while l1 and l2:
            p.next = ListNode(l1.val + l2.val + carry)
            carry = p.next.val // 10
            p.next.val = p.next.val % 10
            p = p.next
            l1 = l1.next
            l2 = l2.next

        res = l1 or l2
        while res:
            p.next = ListNode(res.val + carry)
            carry = p.next.val // 10
            p.next.val = p.next.val % 10
            p = p.next
            res = res.next

        if carry:
            p.next = ListNode(carry)

        return dummy.next


s = Solution()


l1 = SingleLinkedList()
l1.add(ListNode(2))
l1.add(ListNode(3))
l1.add(ListNode(4))

l2 = SingleLinkedList()
l2.add(ListNode(8))
l2.add(ListNode(9))
l2.add(ListNode(6))
l2.add(ListNode(9))

r = s.add_two_number(l1.head, l2.head)

while(r):
    print(r.val)
    r = r.next


