from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.listse_controller import app_list_se
from controller.listde_controller import app_list_de
from controller.listse_circle_controller import app_list_se_circle

app = Flask(__name__)
app.register_blueprint(app_student)

app = Flask(__name__)
app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
app.register_blueprint(app_list_de)
app.register_blueprint(app_list_se_circle)


if __name__ == '__main__':
    app.run()
