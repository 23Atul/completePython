
# insert new node at head

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def inserAtHead(head,data):


    newNode=Node(data)

    if head is None:
        return newNode

    newNode.next=head

    head=newNode

    return head


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)



head=Node(99)
head=inserAtHead(head,200)

head=inserAtHead(head,10000)

print_linked_list(head)
