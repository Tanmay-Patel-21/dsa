class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    sumNode = Node()
    sumCurrent = sumNode
    carry = 0
    while head1 is not None and head2 is not None:
        temp = Node()
        sum = head1.data+head2.data+carry
        temp.data = sum % 10
        carry = sum//10
        sumNode.next = temp
        sumNode = sumNode.next
        head1 = head1.next
        head2 = head2.next

    if head1 is not None:
        while head1 is not None:
            temp = Node()
            sum = head1.data+carry
            temp.data = sum % 10
            carry = sum//10
            sumNode.next = temp
            sumNode = sumNode.next
            head1 = head1.next

    if head2 is not None:
        while head2 is not None:
            temp = Node()
            sum = head2.data+carry
            temp.data = sum % 10
            carry = sum//10
            sumNode.next = temp
            sumNode = sumNode.next
            head2 = head2.next

    if carry > 0:
        temp = Node()
        temp.data = carry
        sumNode.next = temp

    return sumCurrent.next
