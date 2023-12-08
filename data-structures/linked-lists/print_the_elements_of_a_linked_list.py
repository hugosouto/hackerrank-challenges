'''
Challenge: Print the Elements of a Linked List
Difficulty: Easy
Topic: Problem Solving (Basic)
Max Score: 5
Success Rate: 97.20%
Task: Get started with Linked Lists!
Problem: https://www.hackerrank.com/challenges/[...]/problem
'''

# Imports
import math
import os
import random
import re
import sys
import tempfile
from io import StringIO

# Funtions
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Simulate input from HackerRank
raw_data = '''2
16
13
'''
    # Expected Output:
    # 16
    # 13

# Data
input = StringIO(raw_data)

# Function
def printLinkedList(head):
    return None

# Main
if __name__ == '__main__':
    fptr = tempfile.NamedTemporaryFile(mode='w')
    
    llist_count = int(input.readline())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input.readline())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)

    fptr.close()