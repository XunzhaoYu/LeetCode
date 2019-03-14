"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(self, l1, l2):  # 24 ms less than 100.00%, 10.9 MB less than 30.42%
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    elif not l2:
        return l1
    pointer1, pointer2 = l1, l2
    current = l1
    if l1.val < l2.val:
        current = l1
        pointer1 = pointer1.next
    else:
        current = l2
        pointer2 = pointer2.next
    res = current
    while pointer1 and pointer2:
        if pointer1.val < pointer2.val:
            current.next = pointer1
            pointer1 = pointer1.next
        else:
            current.next = pointer2
            pointer2 = pointer2.next
        current = current.next
    current.next = pointer1 if pointer1 else pointer2
    return res


def mergeTwoLists2(self, l1, l2):  # recursion function
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2


def mergeTwoLists(self, l1, l2):  # save memory space
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 or not l2:
        return l1 or l2  # *** or 的运用

    preroot = ListNode(-1)  # dummy node
    node = preroot  # node equivalent to "current"

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    node.next = l1 or l2  # again, the use of "or"


