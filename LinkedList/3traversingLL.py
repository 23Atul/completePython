# traversing LinkedList Nodes

class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


# creating nodes
head = Node(30)
second = Node(50)
third = Node(100)
forth = Node(199)

# linking nodes
head.next = second
second.next = third
third.next = forth


# traversing nodes
# we can't loose head so we can do head=head.next so we assign it to a new variable and head reference is always present

curr = head
while curr is not None:  # iterate till last node (None) is not reached
    print(curr.data)
    curr=curr.next #this lines updates the value of curr with the address of next node everytime