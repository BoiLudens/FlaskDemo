# from flask import Flask
#
# app = Flask(__name__)
#
# from app import routes
#
# app.run(debug=True)
from flask import Flask


def create_app():
    app = Flask(__name__)
    from src.routes import hello as hello_blueprint
    app.register_blueprint(hello_blueprint)
    return app
