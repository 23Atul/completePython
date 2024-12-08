
#  enter a new node at specific position  (0 based indexing )

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def insertAtPosition(head, data, position):

    newNode=Node(data)

    if position ==0:  # if user want to insert newnode at first, make it head
        newNode.next=head
        head= newNode
        return head


    curr=head
    
    for _ in range(position-1):  # Traverse to the node just before the target position


        if curr is None:
            # Handle invalid position
            raise IndexError("Position out of bounds")
        curr = curr.next

    newNode.next=curr.next
    curr.next=newNode


    return head


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)


head=Node(10)

n1=Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(50)

head.next=n1
n1.next=n2
n2.next=n3
n3.next=n4

print_linked_list(head)

head=insertAtPosition(head, 800, 4)

print_linked_list(head)