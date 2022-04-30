from model.student import Student
from model.list_de import ListDE
from model.node_de import NodeDE

class ListDEservice:
    cities = ["manizales", "pereira", "chinchina", "armenia"]

    def __init__(self):
        self.students = ListDE()
#
    def get_all_students(self):
        if self.students.head == None:
            return{"message": "lista sin datos"}
        return self.students.get_all_students()

#
    def add_student(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_student(student)
        else:
            raise Exception("la ciudad no es valida")

#
    def add_to_start(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("la ciudad no es valida")

#

    def delate_student_id(self,id):
        self.students.delate_student_id(id)
        return{"messahe":"eliminaado correctamente por id"}


#
    def invert(self):
        if self.students.head == None:
            return {"message": "La lista està vacia"}
        else:
            self.students.invert()
            return {"message": " se ha invertido la lista "}

#

    def eliminate_student_position(self,position):
        self.students.delete_student_by_position(position)
        return {"message":"eliminado correctamente"}

#
    def woman_first(self):
        if self.students.head == None:
            return {"message": " no hay datos "}
        else:
            self.students.woman_first_de()
            return {"message": "colocacion mujeres primero correctamente"}

#
    def group_intercalate(self):
        self.students.group_intercalate()
        return {"message": "intercalada correctamente"}


#



