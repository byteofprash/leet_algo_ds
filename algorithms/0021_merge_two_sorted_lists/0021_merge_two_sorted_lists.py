"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """ merge two lists

    :param l1: TODO
    :param l2: TODO
    :returns: TODO

    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if not l1 and l2:
        return None
    newlist_head = ListNode(0)
    newlist_start = newlist_head
    while l1 and l2:
        if l1.val <= l2.val:
            print(l1.val, l2.val)
            newval = ListNode(l1.val)
            newlist_head.next = newval
            l1 = l1.next
        elif l1.val > l2.val:
            print(l1.val, l2.val)
            newval = ListNode(l2.val)
            newlist_head.next = newval
            l2 = l2.next
        newlist_head = newlist_head.next
    newlist_head.next = l1 or l2
    return newlist_start.next


val = ListNode(1)
val2 = ListNode(2)
val3 = ListNode(4)

al = ListNode(0)
al2 = ListNode(3)
al3 = ListNode(4)

val.next = val2
val2.next = val3

al.next = al2
al2.next = al3

ret = mergeTwoLists(val, al)

text = ""
while ret.next:
    text = text + str(ret.val) + "->"
    ret = ret.next
print(text + str(ret.val))

