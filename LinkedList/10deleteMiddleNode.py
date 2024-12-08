
# delete middle node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def deleteMid(head,count):


    if head.next==None:
        head=None
        return head

    curr=head
    mid=count//2

    for _ in range(mid-1):
        curr=curr.next

    curr.next=curr.next.next


    return head


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)


head = Node(10)

n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(50)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print_linked_list(head)


head= deleteMid(head,5)

print_linked_list(head)

