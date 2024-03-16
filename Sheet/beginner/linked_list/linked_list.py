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

    def changeValue(self, index, val):
        current = self.head
        current_pos = 0
        while (current_pos < index):
            current = current.next
            current_pos += 1
        current.value = val

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

    def sort(self, ll):
        if (ll.length > 1):
            mid = ll.length//2
            current = ll.head
            i = 0
            l = LinkedList()
            r = LinkedList()
            while current and i < ll.length:
                if (i < mid):
                    l.addNode(LinkedNode(current.value))
                else:
                    r.addNode(LinkedNode(current.value))
                current = current.next
                i += 1
            self.sort(l)
            self.sort(r)
            i, j, k = 0, 0, 0
            l_curr, r_curr = l.head, r.head
            while (i < l.length and j < r.length):
                if (l_curr.value <= r_curr.value):
                    ll.changeValue(k, l_curr.value)
                    l_curr = l_curr.next
                    i += 1
                else:
                    ll.changeValue(k, r_curr.value)
                    r_curr = r_curr.next
                    j += 1
                k += 1
            while (i < l.length):
                ll.changeValue(k, l_curr.value)
                l_curr = l_curr.next
                i += 1
                k += 1

            while (j < r.length):
                ll.changeValue(k, r_curr.value)
                r_curr = r_curr.next
                j += 1
                k += 1
            # while (i < l.length and j < r.length):
            #     if (l[i] <= r[j]):
            #         arr[k] = l[i]
            #         i += 1
            #     else:
            #         arr[k] = r[j]
            #         j += 1
            #     k += 1
            # while (i < len(l)):
            #     arr[k] = l[i]
            #     i += 1
            #     k += 1

            # while (j < len(r)):
            #     arr[k] = r[j]
            #     j += 1
            #     k += 1

    def merge(self, l1, l2):
        pass


lf = LinkedLinkFunctions()
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
ll = LinkedList()
for i in arr:
    ll.addNode(LinkedNode(i))
# ll.changeValue(3, 69)
lf.sort(ll)
ll.printList()
# print(arr)
