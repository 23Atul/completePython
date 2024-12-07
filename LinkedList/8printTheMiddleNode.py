
# print the data of middle node of the linked list


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def findLength(head):
    count=0
    if head is None:
        return None
    if head.next is None:
        return 1
    
    curr=head
    while curr is not None:
        count+=1
        curr=curr.next


    return count


def findMid(head,count):

    # count=findLength(head)      #if count is not given and only head is given then we can do this

    if count is None:
        return None
    if count ==1:
        return head.data
    

    mid = count//2
    curr=head

    for _ in range(mid):
        curr=curr.next


    return curr.data


def print_linked_list(head):
    cur = head
    result = ""
    while cur is not None:
        result += str(cur.data) + " -> "
        cur = cur.next
    result += "None"
    print(result)




head=Node(60)
n2=Node(80)
n3 = Node(90)
n4 = Node(100)
n5 = Node(180)
n6 = Node(830)
n7 = Node(700)

head.next=n2
n2.next=n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

print_linked_list(head)

count=findLength(head)

print(count)


print(findMid(head,count))






