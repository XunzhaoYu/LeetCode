"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

    begin to intersect at node c1.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    Output: Reference of the node with value = 8
    Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:
    Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Reference of the node with value = 2
    Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: null
    Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
    Explanation: The two lists do not intersect, so return null.


Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getIntersectionNode(headA, headB):   # Exceed Time Limit
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    currA, currB = headA.next, headB.next
    if not currA or not currB:
        return null
    end, res = None, None
    while currA is not headA:
        if not currA.next:
            currA.next = headB
            end = currA
        if not currB.next:
            currB.next = headA
        currA = currA.next
        currB = currB.next
        if currA is currB:
            res = currA
            break
    while currA is not end:
        currA = currA.next
    while currB is not end:
        currB = currB.next
    currA.next = None
    currB.next = None
    return res


def getIntersectionNode2(headA, headB):  # best solution from all submissions, tested 208 ms, faster than 68.13%
    if headA is None or headB is None:
        return None
    pa = headA  # 2 pointers
    pb = headB
    while pa is not pb:
        # if either pointer hits the end, switch head and continue the second traversal,
        # if not hit the end, just move on to next
        pa = headB if pa is None else pa.next  # *** 2 pointers idea, and if else.
        pb = headA if pb is None else pb.next
    return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None
