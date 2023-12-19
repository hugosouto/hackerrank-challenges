

Max Score: 5
Success Rate: 

'''
Challenge: Insert a Node at the Tail of a Linked List
Difficulty: Easy
Topic: Problem Solving (Intermediate)
Max Score: 5
Success Rate: 95.26%
Task: Create and insert a new node at the tail of a linked list.
Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
'''

import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Simulate input from HackerRank
raw_data = '''
'''
    # Expected Output:
    # 

# Data
input = StringIO(raw_data)


# Function
def insertNodeAtTail(head, data):
    return

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    llist_count = int(input.readline())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input.readline())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
