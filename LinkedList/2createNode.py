
# create a LL with 5 nodes and link them and access them

# creating Node class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


# creating objec of class Node
head = Node(10)
n2 = Node(20)

n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# linking the nodes to form a LinkedList
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# head --> n2 --> n3 --> n4 --> n5
# 10 --> 20 --> 30 --> 40 --> 50


# accessing data through node
print(head.data) #10
print(n2.data) #20
print(n3.data) #30
print(n4.data) #40
print(n5.data) #50

# accessing data through address
print(head.next.data) # n2.data  => 20
print(n2.next.data) # n3.data  => 30
print(n3.next.data) #n4.data  => 40
print(n4.next.data) #n5.data => 50


print(head.next.next.data)  #n2.next.data =>  n3.data => 30
