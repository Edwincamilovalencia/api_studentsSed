from model.student import Student
import json

class StudentService:
    students = []
    cities=["Manizales","Pereira","Chinchina","Armenia"]


    def __init__(self):
        self.students = []
        carloaiza = Student({"idenfication":"75147236","name":"Carlos"})
        self.students.append(carloaiza)


    def get_all_students(self):
        return self.students

    def get_percentage_students_by_gender(self, gender):
        count = 0
        for student in self.students:
            if student.gender == gender:
                count = count + 1
        return count / len(self.students)

    def get_porcentaje_students_jos_avr_salary(self, gender):
        contador = 0
        sum_salary = 0
        for student in self.students:
            if student.job == True and student.gender == gender:
                contador = contador + 1
                sum_salary = sum_salary+student.salary

        return{"salario promedio": sum_salary/contador,
               "cantidad": contador,
               "% trabajan": contador/len(self.students)}
# 1
    def get_porcentaje_estudiantes(self,gender,salary):

        lista_sola=[]
        for student in self.students:
            if student.gender == gender and student.salary > salary:
                lista_sola.append(student.__dict__)
        return(lista_sola)


# 2
    def get_lista_hombre_mujer_mas_ganan(self, gender):
        listaSalarios=[]
        for student in self.students:
            if student.gender == gender:
                listaSalarios.append(student.salary)
        salarioMasAlto=listaSalarios[0]
        for x in listaSalarios:
            if x > salarioMasAlto:
                salarioMasAlto=x
        for student in self.students:
            if student.salary == salarioMasAlto:
                return (student.__dict__)
#3
    def get_listado_salarios_en_un_rango(self,salariomin,salariomay):
        rango_salario = []
        for student in self.students:
            if student.salary >= salariomin and student.salary <= salariomay:
                rango_salario.append(student.__dict__)
        return (rango_salario)


#4
    def get_procentaje_promedio_students_salary(self,gender):
        contador = 0
        salario_prome = 0
        for student in self.students:
            if student.job == True and student.gender == gender:
                contador = contador + 1
                salario_prome = salario_prome + student.salary
        return {"salario promedio": salario_prome /contador}

#ejercicio en clase / evaluacion conceptos

    def get_promedio_students_edad_ubicacion(self):
        estudiantes_ubicacion = []

        edad_prome = 0
        for student in self.students:
            if student.age == student.age:
                edad_prome = edad_prome + student.age
                promedio= edad_prome/len(self.students)
        for student in self.students:
            if student.location ==1 and student.age > promedio:
                estudiantes_ubicacion.append(student.__dict__)
        return(estudiantes_ubicacion)

#
    def get_dict_cities(self):
        dict_cities={}
        for city in self.cities:
            dict_cities[city]=[0,0]
        return dict_cities

    def get_students_by_city(self):
        dict_cities = self.get_dict_cities()
        for student in self.students:
            if student.job:
                dict_cities[student.city][0]=dict_cities[student.city][0]+1
            else:
                dict_cities[student.city][1] = dict_cities[student.city][1] + 1
        return dict_cities









