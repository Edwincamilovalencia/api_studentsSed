from service.list_de_circle_service import List_DE_CRService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service import list_de_circle_service

app_list_de_circle = Blueprint("app_list_de_circle",__name__)
list_de_circle_service = List_DE_CRService()



@app_list_de_circle.route('/list_de_circle', methods=['POST'])
def add_de_circle():
    try:
        data = request.json
        list_de_circle_service.add_de_circle(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")


@app_list_de_circle.route('/list_de_circular/addtostart',methods=['POST'])
def add_to_start_circular_de():
    try:
        data = request.json
        list_de_circle_service.add_to_start_circular_de(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de_circle.route('/list_de_circle/all')
def get_all_students_circular_de():

    return Response(status=200,
                    response=json.dumps(get_all_students_circular_de.get_all_students_circular_de()
                    ,cls=UtilEncoder),mimetype="application/json")