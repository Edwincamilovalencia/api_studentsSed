from model.student import Student
from model.list_se import ListSE

class ListSEServicecircle:
    cities = ["manizales", "pereira", "chinchina", "armenia"]

    def __init__(self):
        self.students=ListSE()
#
    def add_circle(self,data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add(student)
        else:
            raise Exception("la ciudad no es valida")

#
    def add_student_to_start_circle(self, data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("la ciudad no es valida")


