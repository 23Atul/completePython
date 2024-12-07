class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def lengthOfLL(head):
    if head is None:
        return None
    
    if head.next is None:
        return 1
    
    curr=head
    count=0

    while curr is not None:
        count+=1
        curr=curr.next


    return count

head=None

print(lengthOfLL(head)) # None
head = Node(20)

print(lengthOfLL(head)) # 20  ==>1

n1=Node(50)
head.next=n1

print(lengthOfLL(head)) # 20 --> 50  ==>2

n2=Node(90)
n1.next=n2

print(lengthOfLL(head)) # 20 --> 50 --> 90  ==> 3

n3=Node(120)
n2.next=n3

print(lengthOfLL(head))  #20 --> 50 --> 90 --> 120   ==>4


