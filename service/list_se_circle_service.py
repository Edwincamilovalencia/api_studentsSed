from model.student import Student
from model.list_secircle import Listacircularse


class Listcircular_seService:
    cities = ["manizales", "pereira", "chinchina", "armenia"]

    def __init__(self):
        self.students=Listacircularse()


    def add_student_circle(self,data:Student):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_student_circle(student)
        else:
            raise Exception("la ciudad no es valida")

    def get_all_students_circular(self):
        return self.students.get_all_students_circular()


    def add_student_to_start_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_student_to_start_circular(student)
        else:
            raise Exception("La ciudad no está en la lista")


    def count(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        return self.students.count()


