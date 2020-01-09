"""
STATUS: Needs optimization
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(nums):
    """returns a list node

    :param nums: TODO
    :returns: TODO

    """
    return_node = ListNode(int(nums[0]))
    prev_node = return_node
    for i in range(1, len(nums)):
        curr_node = ListNode(int(nums[i]))
        prev_node.next = curr_node
        prev_node = curr_node
    return return_node


def addTwoNumbers(l1, l2):
    """Solution

    :param l1: TODO
    :param l2: TODO
    :returns: TODO

    """
    l1_val = ""
    while l1.next is not None:
        l1_val += str(l1.val)
        l1 = l1.next
    l1_val +=str(l1.val)
    l1_val = l1_val[::-1]

    l2_val = ""
    while l2.next is not None:
        l2_val += str(l2.val)
        l2 = l2.next
    l2_val +=str(l2.val)
    l2_val = l2_val[::-1]

    return_val = int(l1_val) + int(l2_val)
    return_val = str(return_val)[::-1]
    if len(return_val) < 1:
        return ListNode(int(return_val[0]))
    else:
        return_node = ListNode(int(return_val[0]))
        prev_node = return_node
        for i in range(1, len(return_val)):
            curr_node = ListNode(int(return_val[i]))
            prev_node.next = curr_node
            prev_node = curr_node

        return return_node


l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])
print(addTwoNumbers(l1, l2))
