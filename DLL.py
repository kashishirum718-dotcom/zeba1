class node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = node(data)
            self.start_node = new_node
        else:
            print("List is not empty")
    def InsertToEnd(self, data):
        new_node = node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = new_node
        new_node.prev = n
    def DeleteAtStart(self):
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None
    def delete_at_end(self):
        if self.start_node is None:
            print("The linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        n = self.start_node
        while n is not None:
            print("Element is:", n.item)
            n = n.next
        print()
NewDoublyLinkedList = doublyLinkedList()
NewDoublyLinkedList.InsertToEmptyList(10)
NewDoublyLinkedList.InsertToEnd(20)
NewDoublyLinkedList.InsertToEnd(30)
NewDoublyLinkedList.InsertToEnd(40)
NewDoublyLinkedList.Display()
NewDoublyLinkedList.DeleteAtStart()
NewDoublyLinkedList.delete_at_end()
NewDoublyLinkedList.Display()