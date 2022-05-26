from model.student import Student
from .node_de import NodeDE

class list_circle_de:

    def _init_(self):
        self.head=None
        self.last=None

#Validar existencia
    def empty(self):
        if self.head==None:
            return True
        else:
            return False

#Agregar
    def add_de_circle(self,data):
        if self.empty():
            self.head=self.last=NodeDE(data)
        else:
            temp=self.last
            self.last=temp.next=NodeDE(data)
            self.last.previous=temp

#Agregar al inicio


    def add_to_start_circular_de(self,data):
        if self.empty():
            self.head=self.last=NodeDE
        else:
            temp=NodeDE
            temp.next=self.head
            self.head.previous=temp
            self.head=temp

#listar
    def get_all_students_circular_de(self):
        list = []
        temp = self.head
        while temp.next != self.head:
            list.append(temp.data)
            temp = temp.next
        list.append(temp.data)
        return list