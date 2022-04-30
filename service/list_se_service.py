from model.student import Student
from model.list_se import ListSE
from model.node import Node

class ListSEService:
    cities = ["manizales", "pereira", "chinchina", "armenia"]

    def __init__(self):
        self.students=ListSE()

    def get_all_students(self):
        return self.students.head

#
    def add_student(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add(student)
        else:
            raise Exception("la ciudad no es valida")

#
    def add_student_to_start(self, data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("la ciudad no es valida")
#
    def invert(self):
        if self.students.head== None:
            return{"message":"La lista està vacia" }
        else:
            self.students.invert()
            return {"message":" se ha invertido la lista " }
#
    def add_to_position(self,position,Student):
        try:
            self.students.add_to_position(position,(Student))
            return {"message":"Adicionado con éxito"}
        except Exception as e:
            return {"message": str(e)}

#
    def insert_at_end(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.insert_at_end(student)
        else:
            raise Exception("la ciudad no es valida")
#
    def eliminate_data(self,id):
        self.students.delate_student(id)
        return {"message": "elominado correctamente" }
#
    def eliminate_student_position(self, p):
        self.students.delete_student_position(p)
        return{"message":"eliminado correctamente "}

#
    def woman_first(self):
        if self.students.head== None:
            return {"message":" no hay datos "}
        else:
            self.students.woman_first()
            return {"message":"colocacion mujeres primero correctamente"}


#
    def group_intercalate(self):
        self.students.group_intercalate()
        return {"message": "intercalada correctamente"}









