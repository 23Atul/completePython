class Node:
    def __init__(self,data):

        self.data=data
        self.next=None
        

def deleteHead(head):

    if head is None:
        return None
    
    head=head.next

    return head


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)

head=Node(40)
n1=Node(60)
n2=Node(100)

head.next=n1
n1.next=n2
print_linked_list(head)
head=deleteHead(head)

print_linked_list(head)





