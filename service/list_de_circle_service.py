from model.list_de_circle import list_circle_de
from model.student import Student

class List_DE_CRService:
    cities = ["manizales", "pereira", "chinchina", "armenia"]

    def _init_(self):
        self.students=List_DE_CRService()

    def add_de_circle(self,data:Student):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_de_circle(student)
        else:
            raise Exception("la ciudad no es valida")

    def add_to_start_circular_de(self, data):
        student = Student(data)
        if data["city"] in self.cities:
            self.students.add_to_start_circular_de(student)
        else:
            raise Exception("la ciudad no es valida")

    def get_all_students_circular_de(self):
        return self.students.get_all_students_circular_de()