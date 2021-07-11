"""

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node


    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)


a_list = LinkedList()

a_list.append(1)
a_list.append(2)
a_list.append(3)
a_list.display()
