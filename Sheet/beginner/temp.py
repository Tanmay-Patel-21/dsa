from linked_list import LinkedList, LinkedNode


l1 = LinkedList()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for val in values:
    l1.addNode(LinkedNode(val))

l1.printList()
