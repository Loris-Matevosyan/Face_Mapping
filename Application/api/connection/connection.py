from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from waitress import serve



class ApiConnection():

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        #Must be secret
        self.app.config["JWT_SECRET_KEY"] = "super_secret_key"
        # Must be secret
        self.jwt = JWTManager(self.app)


    def getApi(self):
        return self.api


    def initialize(self):
        serve(self.app, host="127.0.0.1", port=5001)
