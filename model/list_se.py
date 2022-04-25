from .node import Node
from model.student import Student

class ListSE:
    def __init__(self):
        self.head = None
        self.count=0


    def add(self,data):
        if self.head == None:
            self.head = Node(data)
        else:

            #posicionados en el ultimo
            temp=self.head
            while temp.next != None:
                temp = temp.next

            #posicionados en el ultimo

            temp.next = Node(data)
    def add_to_start(self,data:Student):
        if self.head == None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next =self.head
            self.head=temp

    def invert(self):
        if self.head != None:     #verifica i hay algo
            list_cp=ListSE()     # crea una lista copia de listSE()
            temp=self.head
            while temp != None:
                list_cp.add_to_start(temp.data)
                temp=temp.next
                self.head=list_cp.head

    def validate_exist(self,id):
        temp =self.head
        while temp != None:
            if temp.date.identification == id:
                return True
            temp =temp.next
        return False

    def add_to_position(self, position: int, student: Student):
        if position > 0 and position <= (self.count + 1):
            if position == 1:
                new_node = Node(student)
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        new_node = Node(student)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count = +1
                        break
                    temp = temp.next
                    count = +1
            self.count = +1
        else:
            raise Exception("La posición no es válida")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n= self.head_node
        while n.ref is not None:
            n = n.next
        n.next = new_node;