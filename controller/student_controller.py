from flask import Response, Blueprint, jsonify, json
from service.student_service import StudentService
from util.util_encoder import UtilEncoder

app_student = Blueprint("app_student", __name__)

@app_student.route ('/student/all')
def get_all_students():
    student_service = StudentService()
    return Response(status=200,
                    response=json.dumps(student_service.get_all_students(),
                                        cls=UtilEncoder),
                    mimetype="application/json"
                    )
    #return jsonify(student_service.get_all_students_dict())

@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_students_by_gender(gender):
    student_service = StudentService()
    return str(student_service.get_percentage_students_by_gender(int(gender)))

@app_student.route('/student/per_students_job_avgsalary/<gender>')
def get_porcentaje_students_job_avr_salary(gender):
    student_service = StudentService()
    return jsonify(student_service.get_porcentaje_students_jos_avr_salary(int(gender)))

#1
@app_student.route("/student/rango_sueldo/<gender>/<salary>")
def get_porcentaje_estudiantes(gender,salary):
    student_service=StudentService()
    return jsonify(student_service.get_porcentaje_estudiantes(int(gender),int(salary)))

#2

@app_student.route("/student/SueldoMayor/<gender>")
def get_lista_hombre_mujer_mas_ganan(gender):
    student_service=StudentService()
    return jsonify(student_service.get_lista_hombre_mujer_mas_ganan(int(gender)))

#3
@app_student.route("/student/rango_sueldos_hombre_mujer/<salariomin>/<salariomay>")
def get_listado_salarios_en_un_rango(salariomin,salariomay):
    student_service = StudentService()
    return jsonify(student_service.get_listado_salarios_en_un_rango(int(salariomin),int(salariomay)))


#4
@app_student.route("/student/salary_promedio/<gender>")
def get_procentaje_promedio_students_salary(gender):
    student_service=StudentService()
    return jsonify(student_service.get_procentaje_promedio_students_salary(int(gender)))

#ejercicio en clase
@app_student.route("/student/age_promedio_location")
def get_promedio_students_edad_ubicacion():
    student_service=StudentService()
    Response(status=200,
             response=json.dumps(student_service.get_promedio_students_edad_ubicacion(),
                                 cls=UtilEncoder),
             mimetype="application/json"
             )
    #return jsonify(student_service.get_promedio_students_edad_hubicacion(self))


#segundo ejercicio en clase
@app_student.route("/student/lugar_trabajo_estudiante")
def get_students_by_city():
    student_service=StudentService()
    return jsonify(student_service.get_students_by_city())

