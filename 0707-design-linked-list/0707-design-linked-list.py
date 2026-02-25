class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()   
        self.count_node = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count_node:
            return -1

        current = self.head.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.count_node += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        current = self.head

        while current.next:
            current = current.next

        current.next = node
        self.count_node += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.count_node:
            return

        node = Node(val)
        current = self.head

        for _ in range(index):
            current = current.next

        node.next = current.next
        current.next = node
        self.count_node += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count_node:
            return

        current = self.head

        for _ in range(index):
            current = current.next

        current.next = current.next.next
        self.count_node -= 1