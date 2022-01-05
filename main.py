class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def values(self):
        return [node.value for node in self]

    def insert(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple_nodes(self, values):
        for value in values:
            self.insert(value)

    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def print(self):
        p = self.head
        while p is not None:
            print(p.value, end=' ')
            p = p.next


def doubles(L: LinkedList):
    p = L.head
    howManyElements = 0
    helperList = LinkedList()

    while p is not None:
        helperList.insert(p.value)
        howManyElements += 1
        p = p.next

    p = L.head
    j = helperList.head

    moreThanOnce = 0

    duplicatedList = LinkedList()

    temp = 0
    while j is not None:
        while p is not None:
            if j.value == p.value:
                temp += 1
            p = p.next
        if temp != 1:
            duplicatedList.insert(j.value)

        j = j.next
        p = L.head
        temp = 0

    return duplicatedList


if __name__ == "__main__":

    myList = LinkedList()

    valueArray = [4, 2, 3, 4, 7, 2, 9, 18, 18, 139, 293, 3]

    i = 0

    while i != len(valueArray):
        myList.insert(valueArray[i])
        i += 1

    myNewList = doubles(myList)
    myNewList.print()
