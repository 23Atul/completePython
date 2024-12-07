
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtTail(head, data):

    nodeN = Node(data)

    if head is None:  # edge case for head if head is not assigned any object value
        return nodeN

    curr = head

    # moving to next node and stopping to last node....just like stopping at n-1 and not n in loop
    while curr.next is not None:
        curr = curr.next

    curr.next = nodeN
    return head


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)


# head = Node(10)
# n2 = Node(20)
# n3 = Node(30)

# head.next = n2
# n2.next = n3

# curr = head
# while curr is not None:
#     print(curr.data)
#     curr = curr.next


head = Node(10)
head = insertAtTail(head, 100)
head = insertAtTail(head, 200)
head = insertAtTail(head, 300)
head = insertAtTail(head, 1800)


print_linked_list(head)
