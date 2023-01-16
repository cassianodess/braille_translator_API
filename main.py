from flask import Flask, request, make_response
from app.controllers.translator.translator import translator_blueprint
from os import getenv
app = Flask(__name__)

app.register_blueprint(translator_blueprint)


@app.before_request
def middleware():
    
    authorization = request.headers.get("Authorization").split(" ")[1] if request.headers.get("Authorization") else None

    if request.method != "OPTIONS" and not authorization == getenv("SECRET"):
        return make_response({"message": "Unauthorized"}), 401