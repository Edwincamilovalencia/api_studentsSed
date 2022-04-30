from service.list_se_service import ListSEService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service import list_se_service

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()



#
@app_list_se.route('/list_se/all')
def get_all_students():
    return Response(status=200,
                    response=json.dumps(list_se_service.get_all_students(),
                    cls=UtilEncoder),mimetype="application/json")


#
@app_list_se.route('/list_se',methods=['POST'])
def save_student():
    data = request.json
    try:
        list_se_service.add_student(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                        mimetype="application/json")
#ciudad no validad abajo
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")


#
@app_list_se.route('/list_se/addtostar',methods=['POST'])
def save_student_to_start():
    data = request.json
    try:
        list_se_service.add_student_to_start(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                        mimetype="application/json")
#ciudad no valida
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")

#
@app_list_se.route('/list_se/invert')
def invert():
    return Response(status=200,
                    response=json.dumps(list_se_service.invert()),mimetype="application/json")
#
@app_list_se.route("/listse/toposition/<position>",methods=["POST"])
def add_to_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_service.add_to_position(int(position),request.json)),
                    mimetype="application/json")


#
@app_list_se.route('/list_se/addtoend',methods=['POST'])
def insert_at_end():
    data = request.json
    try:
        list_se_service.insert_at_end(data)
        return Response(status=200,response=json.dumps({"message":"Adicionado exitosamente"}),
                        mimetype="application/json")
#ciudad no valida
    except Exception as e:
        return Response(status=409, response=json.dumps({"message": str(e)}),
                        mimetype="application/json")

#

@app_list_se.route('/list_se/delate_student/<id>')
def eliminate_data(id):
    return Response(status=200,
                    response=json.dumps(list_se_service.eliminate_data(int(id))),
                    mimetype="application/json")


#
@app_list_se.route('/list_se/delate_student_position/<position>')
def eliminate_student_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_service.eliminate_student_position(int(position))),
                    mimetype="application/json")


#
@app_list_se.route('/list_se/woman_firts')
def woman_first():
    return Response(status=200,
                    response=json.dumps(list_se_service.woman_first()),
                    mimetype="application/json")



#
@app_list_se.route('/list_se/group_intercalate')
def group_intercalate():
    return Response(status=200,
                    response=json.dumps(list_se_service.group_intercalate()),
                    mimetype="application/json")




#####
@app_list_se.route('/list_se/operators_order')
def operators_order():
    return Response(status=200,
                    response=json.dumps(list_se_service.operators_order()),
                    mimetype="application/json")



