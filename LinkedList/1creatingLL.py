
# creating a linked list

class Node:
    def __init__(self,data):  #constructor function
        self.data=data
        self.next=None
        


v1=Node(10)

v2=Node(20)

v1.next=v2

print(v1) #address of v1
print(v2) #addrress of v2

print(v1.next)  #address of v2

print(v1.next.data)  #20
