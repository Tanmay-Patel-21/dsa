class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

        if head is not None:
            self.length = 1
        else:
            self.length = 0

    def addNode(self, newNode):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        self.length += 1

    def delNode(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            self.length -= 1
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None
            self.length -= 1

    def insertNodeAtPos(self, node, pos):
        if pos > self.length:
            raise IndexError
        elif pos == self.length:
            self.addNode(node)
            return

        current = self.head
        current_pos = 0
        while (current_pos < pos-1):
            current = current.next
            current_pos += 1
        node.next = current.next
        current.next = node

    def printList(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print("-->", end="")
        print()


class LinkedLinkFunctions:
    def __init__(self):
        pass

    def sort(l):
        pass

    def merge(l1, l2):
        pass
