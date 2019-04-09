"""
Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false

Example 2:
    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def isPalindrome(head):  # 76 ms, faster than 61.40%. time: O(n), space: O(n)
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
        return True
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    length, i = len(stack) - 1, 0
    while i < (length - i):
        if stack[i] != stack[length - i]:
            return False
        else:
            i += 1
    return True


def isPalindrome2(head):  # 76 ms, faster than 61.40%. time: O(n), space: O(1)
    if not head:
        return True
    length, prev, curr = 1, head, head
    while prev.next:
        prev = prev.next
        length += 1
    for i in range(length / 2):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    if length % 2 == 1:
        curr = curr.next
    while curr:
        if curr.val != prev.val:
            return False
        else:
            prev, curr = prev.next, curr.next
    return True


def isPalindrome3(head):  # 72 ms, faster than 93.50%. time: O(n), space: O(1). Best solution from submissions (68 ms)
    rev = None
    slow = fast = head
    while fast and fast.next:  # *** idea, use fast to find the midpoint of the linked list.
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev
