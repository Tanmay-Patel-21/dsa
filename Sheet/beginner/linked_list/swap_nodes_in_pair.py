# Problem statement
# You are given a singly linked list of integers.

# Your task is to swap every two adjacent nodes, and return the head of the modified, linked list.

# For Example:

# We have a linked list 1->2->3->4->5->6->7 and so on. You are supposed to swap pairs of a linked list like swap (1,2), (3,4), (5,6), and so on.
# Note:
# 1. You may not modify the data in the list’s nodes; only nodes themselves may be changed. Because imagine a case where a node contains many fields, so there will be too much unnecessary swap.

# 2. If a pair of a node does not exist, then leave the node as it is.


from os import *
from sys import *
from collections import *
from math import *

''' 

    Following is the class structure of the Node class:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            
'''


def pairsSwap(head):
    current = head
    prev = None
    if head is not None and head.next is not None:
        head = head.next
    while current is not None and current.next is not None:
        temp1 = current.next
        temp2 = current.next.next
        current.next = temp2
        temp1.next = current
        if prev is not None:
            prev.next = temp1
        else:
            prev = current
        prev = current
        current = current.next
    return head
