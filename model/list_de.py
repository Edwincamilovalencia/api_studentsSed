from .node_de import NodeDE
from model.student import Student



class ListDE:
    def __init__(self):
        self.head = None
        self.count=0

#
    def get_all_students(self):
        list=[]
        temp =self.head
        while temp != None:
            list.append(temp.data)
            temp =temp.next
        list.append(temp)
        return list

#

    def add_student(self,data):
        if self.head is None:
            newnode=NodeDE(data)
            self.head=newnode
            return
        apuntador=self.head
        while apuntador.next is not None:
            apuntador= apuntador.next

        newnode=NodeDE(data)
        apuntador.next = newnode
        newnode.previus = apuntador
#
    def add_to_start(self,data):
        if self.head is None:
            self.listvacia(data)
            return
        else:
            newNodo=NodeDE(data)
            newNodo.next=self.head
            self.head.previous=newNodo
            self.head=newNodo


#
    def delate_student_id(self,id):
        if self.head.data.identification == id:
            if self.head.next ==None:
                self.head = None
                return
        else:
            temp =self.head
            while temp.next != None:
                if temp.data.identification == id:
                    break
                temp=temp.next
            if temp.next != None:
                temp.previus.next = temp.next
                temp.next.previus = temp.previus
            else:
                if temp.data.identification == id:
                    temp.previus.next =None

        self.count = -1

#
    def invert(self):
        if self.head is None:
            print("la lista está vacía")
            return

        apuntador1 = self.head
        apuntador2 = apuntador1.next

        apuntador1.next = None
        apuntador1.previous = apuntador2

        while apuntador2 is not None:
            apuntador2.previous = apuntador2.next
            apuntador2.next = apuntador1
            apuntador1 = apuntador2
            apuntador2 = apuntador2.previus
        self.head = apuntador1

#
    def delete_student_by_position(self, position):
        if position < 0:
            raise Exception("ingrese un numero positivo")
        elif position == 1:
            self.head = self.head.next
        elif position == self.count:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.previus.next = None

        else:
            posicion = 1
            temp = self.head
            while temp.next != None and position != posicion:
                posicion = posicion + 1
                temp = temp.next

            if temp.next != None:
                temp.previus.next = temp.next
                temp.next.previus = temp.previus
        self.count -= 1


#
    def woman_first_de(self):
        list_cp = ListDE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 2:
                list_cp.add_to_start(temp.data)
            if temp.data.gender == 1:
                list_cp.add_student(temp.data)
            temp = temp.next
        self.head = list_cp.head

#

    def group_intercalate(self):
        M=0
        W=0
        list_cp_man = ListDE()
        list_cp_women = ListDE()
        list_cp_intercalate_genders = ListDE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                list_cp_man.add_student(temp.data)
                M=M+1
            if temp.data.gender == 2:
                W=W+1
                list_cp_women.add_student(temp.data)
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
                    list_cp_intercalate_genders.add_student(tempW.data)
                    tempW = tempW.next

            if tempM != None:
                if tempM.data != None:
                    list_cp_intercalate_genders.add_student(tempM.data)
                    tempM = tempM.next
            MayorLongitud = MayorLongitud-1
        self.head = list_cp_intercalate_genders.head

#
























