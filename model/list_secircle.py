from .node import Node
from model.student import Student

class ListSEcircle:
    def __init__(self):
        self.head = None
#

    
    def add_circle(self, data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            temp = self.head
            while temp.next != self.head:

                temp = temp.next
                temp.next = Node(data)
                temp.next.next = self.head

#
    def add_to_start_circle(self,data: Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            temp.next.next = self.head



