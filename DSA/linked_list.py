# from __future__ import annotations
# from typing import Any

# class Node():
#     def __init__(self, data: Any, next_node : Node = None):
#         self.data = data
#         self.next = next_node


# class LinkedList():
#     def __init__(self, head=None) -> None:
#         self.head = head

#     def append(self, data: Any) -> None:
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return


#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def insert(self, data: Any) -> None:
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def print(self) -> None:
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next

#     def remove(self, data : Any) -> None:
#         current_node = self.head
#         if current_node and current_node.data == data:
#             self.head = current_node.next
#             current_node = None
#             return

#         previous_node = None
#         while current_node and current_node.data != data:
#             previous_node = current_node
#             current_node = current_node.next

#         if current_node is None:
#             return

# if __name__ == '__main__':
#     l = LinkedList()
#     l.append(1)
#     l.append(2)
#     l.append(3)
#     l.insert(0)
#     # print(l.head.data)
#     # print(l.head.next.data)
#     # print(l.head.next.next.data)
#     # print(l.head.next.next.next.data)
#     l.print()

#######################################################################
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next

## ref: https://www.programiz.com/dsa/linked-list
