from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token


class Login(Resource):

    def __init__(self):
        self.username = request.json.get("username")
        self.password = request.json.get("password")

        # Must be hidden
        self.users = {"client": "secret_password"}
        # Must be hidden


    def post(self):
        if self.username in self.users and self.users[self.username] == self.password:

            access_token = create_access_token(identity=self.username)
            return jsonify(access_token=access_token)

        else:
            return jsonify({ "message" : "Invalid credentials"}), 401
