"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """ removeNthFromEnd """
    counter = 1
    starting_head = head
    while head.next:
        counter += 1
        head = head.next
    to_remove = counter - n
    head = starting_head
    if to_remove == 0:
        return  head.next
    for i in range(to_remove - 1):
        head = head.next
    head.next = head.next.next
    return starting_head


val = ListNode(1)
val2 = ListNode(2)
val3 = ListNode(3)
val4 = ListNode(4)
val5 = ListNode(5)

val.next = val2
val2.next = val3
val3.next = val4
val4.next = val5

ret = removeNthFromEnd(val, 0)

text = ""
while ret.next:
    text = text + str(ret.val) + "->"
    ret = ret.next
print(text + str(ret.val))
