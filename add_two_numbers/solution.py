# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_node_to_int(x: ListNode) -> int:
    out = 0
    dec_multiplier = 1
    while x is not None:
        out += x.val * dec_multiplier
        x = x.next
        dec_multiplier *= 10
    return out


def int_to_linked_list(x: int) -> ListNode:
    r = x % 10
    next_v = x // 10
    out = ListNode(val=r,
                   next=int_to_linked_list(next_v) if next_v > 0 else None)
    return out


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = int_to_linked_list(list_node_to_int(l1) + list_node_to_int(l2))
        return out
