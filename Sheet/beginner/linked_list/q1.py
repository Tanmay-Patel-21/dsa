from linked_list import LinkedList, LinkedNode, LinkedLinkFunctions


n = int(input("Enter number of linked lists: "))
merged = LinkedList()
lf = LinkedLinkFunctions()
while (n > 0):
    ll = LinkedList()
    for i in [int(ele)for ele in (
            input("Enter space separted linked list values: ")).split(" ")]:
        ll.addNode(LinkedNode(i))
    lf.merge(merged, ll)
    n -= 1
lf.sort(merged)
merged.printList()
