class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def insertInBetween(self, position, data):
        if position < 0:
            raise ValueError("Position must be a non-negative integer.........!")
        newNode = Node(data)
        if position == 0:
            self.insertAtHead(newNode)
            return
        else:
            current = self.head
            for _ in range(position-1):
                if current is None:
                    raise IndexError("Position out of Range .........................!")
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

    def printList(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end=" --> ")
            currNode = currNode.next
        return


llist = LinkedList()

llist.insertAtHead("0")
llist.insertAtEnd("10")
llist.insertAtEnd("20")
llist.insertAtEnd("30")
llist.insertInBetween(2, 15)
llist.reverse()
llist.printList()



