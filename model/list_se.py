from .node import Node
from model.student import Student


class ListSE:
    def __init__(self):
        self.head = None
        self.count=0


#
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
#
    def add_to_start(self,data:Student):
        if self.head == None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next =self.head
            self.head=temp
#

    def invert(self):
        if self.head != None:     #verifica i hay algo
            list_cp=ListSE()     # crea una lista copia de listSE()
            temp=self.head
            while temp != None:
                list_cp.add_to_start(temp.data)
                temp=temp.next
                self.head=list_cp.head
#
    def validate_exist(self,id):
        temp =self.head
        while temp != None:
            if temp.date.identification == id:
                return True
            temp =temp.next
        return False
#
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
#
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n=self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

#
    def delate_student(self,id):
        if id == self.head.data.identification:
            self.head=self.head.next
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data.identification == id:
                    temp.next=temp.next.next
                    break;
                temp=temp.next
#
    def delete_student_position(self,p):
        posicion = 1
        if p == 1 and self.head.data != None:
            self.head = self.head.next

        temp = self.head
        while temp.next != None:
            posicion=posicion+1
            if temp.next.data !=  None and p == posicion:
                temp.next = temp.next.next
                break;
            temp = temp.next

#
    def woman_first(self):
        list_cp = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 2:
                list_cp.add_to_start(temp.data)
            if temp.data.gender == 1:
                list_cp.add(temp.data)
            temp = temp.next
        self.head = list_cp.head

#

    def group_intercalate(self):
        M=0
        W=0
        list_cp_man = ListSE()
        list_cp_women = ListSE()
        list_cp_intercalate_genders = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp_man.add(temp.data)
                M=M+1
            if temp.data.gender == 2:
                W=W+1
                list_cp_women.add(temp.data)
            temp = temp.next

        if M>W:
            MayorLongitud=M
        else:
            MayorLongitud = W

        tempM =list_cp_man.head
        tempW = list_cp_women.head

        while MayorLongitud > 0:


            if tempW != None:
                if tempW.data != None:
                    list_cp_intercalate_genders.add(tempW.data)
                    tempW = tempW.next

            if tempM != None:
                if tempM.data != None:
                    list_cp_intercalate_genders.add(tempM.data)
                    tempM = tempM.next
            MayorLongitud = MayorLongitud-1
        self.head = list_cp_intercalate_genders.head





