from service.list_se_service import ListSEService
from flask import Response,json,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service import list_se_service

app_list_se = Blueprint("app_list_se",__name__)

list_se_service = ListSEService()

@app_list_se.route('/list_secircle/addtostar',methods=['POST'])
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