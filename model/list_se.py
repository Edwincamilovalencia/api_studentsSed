from .node import Node
from model.student import Student

class ListSE:
    def __init__(self):
        self.head = None


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

    
 #


