class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    # prev = None
    # current = head
    # while current:
    #     next_node = current.next
    #     current.next = prev
    #     prev = current
    #     current = next_node
    # return prev
    prev = None
    current = head
    while current:
        current.next, prev, current = prev, current, current.next
    return prev


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print(None)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(f"The original list is : ")
print_list(head)
print(f"The reverse linked list is : ")
print_list(reverse_linked_list(head))