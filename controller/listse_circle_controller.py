from service.list_se_circle_service import Listcircular_seService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service import list_se_circle_service


app_list_se_circle = Blueprint("app_list_se_circle",__name__)



list_se_circle_service = Listcircular_seService()



@app_list_se_circle.route('/list_se_circle', methods=['POST'])
def add_student_circle():
    try:
        data = request.json
        list_se_circle_service.add_student_circle(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")


@app_list_se_circle.route('/list_se_circle/all')
def get_all_students_circular():

    return Response(status=200,
                    response=json.dumps(list_se_circle_service.get_all_students_circular()
                    ,cls=UtilEncoder),mimetype="application/json")


@app_list_se_circle.route('/list_se_circular/addtostart',methods=['POST'])
def add_student_to_start_circular():
    try:
        data = request.json
        list_se_circle_service.add_student_to_start_circular(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_se_circle.route('/list_se_circular/count')
def count():
    return Response(status=200,
                    response=json.dumps(list_se_circle_service.count(),
                                        cls=UtilEncoder), mimetype="application/json")

