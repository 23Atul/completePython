# Delete Y after X

# Description

# You are given the head of a linked list and two integers x and y.

# Traverse the linked list and remove some nodes in the following way:

# 1. Start with the head as the current node.

# 2. Keep the first x nodes starting with the current node.

# 3. Remove the next y nodes

# 4. * Keep repeating steps 2 and 3 until you reach the end of the list.

# Return the head of the modified list after removing the mentioned nod es.


# n=6 x=3 y=2
# input= 2 3 2 5 3 1

# output= 2 3 2 1


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def XafterY(head,N,X,Y):
    if N < X:   # if length of LL is less than X then nothing to delete
        return head

    curr=head
    count=0  #count will increase in every step to check if end is reached or not
    while count < N-1:  # iterate till last node 
        for _ in range(X-1):  # iterate to skip X nodes

            if curr.next is None:  # check if there is any node to iterate next or not
                IndexError("out of bound")
                return head
            curr=curr.next
            count+=1


        for _ in range(Y):  #iterate to delete Y nodes

            if curr.next is None:   # check if any node is there to delete or not
                IndexError("out of bound")
                break
            curr.next=curr.next.next
            count+=1

    return head


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)


head = Node(2)

n1 = Node(3)
n2 = Node(2)
n3 = Node(5)
n4 = Node(3)
n5=Node(1)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next=n5

print_linked_list(head)

head = XafterY(head,4,3,2)

print_linked_list(head)




        


