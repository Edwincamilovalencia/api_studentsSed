from service.list_de_service import ListDEservice
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service import list_de_service

app_list_de = Blueprint("app_list_de",__name__)

list_de_service= ListDEservice()

#
@app_list_de.route('/list_de/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_de_service.get_all_students(),
                    cls=UtilEncoder),mimetype="application/json")


#

@app_list_de.route('/list_de/add_student',methods=['POST'])
def add_student():
    data = request.json
    try:
        list_de_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                        mimetype="application/json")
#ciudad no validad abajo
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")


@app_list_de.route('/list_de/add_to_start',methods=['POST'])
def add_to_start():
    data = request.json
    try:
        list_de_service.add_to_start(data)
        return Response(status=200, response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    # ciudad no validad abajo
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")

#
@app_list_de.route('/list_de/delate_student_id/<id>')
def delate_student_id(id):
    return Response(status=200,
                    response=json.dumps(list_de_service.delate_student_id(id))
                    ,mimetype="application/json")


#
@app_list_de.route('/list_de/invert')
def invert():
    return Response(status=200,
                    response=json.dumps(list_de_service.invert())
                    ,mimetype="application/json")

#
@app_list_de.route('/list_de/delate_student_position/<position>')
def eliminate_student_position(position):
    return Response(status=200,
                    response=json.dumps(list_de_service.eliminate_student_position(int(position))),
                    mimetype="application/json")

#

@app_list_de.route('/list_de/woman_firts')
def woman_first():
    return Response(status=200,
                    response=json.dumps(list_de_service.woman_first()),
                    mimetype="application/json")


#

@app_list_de.route('/list_de/group_intercalate')
def group_intercalate_de():
    return Response(status=200,
                    response=json.dumps(list_de_service.group_intercalate()),
                    mimetype="application/json")
















