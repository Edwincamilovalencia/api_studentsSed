from .node import Node
from model.student import Student

class ListSE:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            temp = self.head
            while temp.next != self.head:

                temp = temp.next
                temp.next = Node(data)
                temp.next.next = self.head

    def add_to_start(self,data: Student):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
