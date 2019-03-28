"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

Follow up:
    Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):  # 48 ms, faster than 34.57%. Also, not constant memory.
    """
    :type head: ListNode
    :rtype: bool
    """
    map = {}
    while head:
        if head.next not in map:
            map[head] = head.next
        else:
            return True
        head = head.next
    return False


def hasCycle2(head):   # 44 ms, faster than 69.08%.  Copied from the best solution.
    if not head:
        return False
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next  # *** idea, fast catching slow.
        return True
    except:
        return False
