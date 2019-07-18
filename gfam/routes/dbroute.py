from flask import Blueprint, jsonify, request, abort
from gfam.services import db_data
from flask_restful import Resource, Api, reqparse

mod1 = Blueprint('api2', __name__)
api2 = Api(mod1)


class SequenceData(Resource):
    """
    #Main class to get, post, delete, put sequence data
    """
    def get(self):
        sequence_name = request.args.get('sequence_name')
        # id = request.args.get('id')
        # print(sequence_name)
        # try:
        #     val = int(sequence_name)
        # except Exception as e:
        #     print("ERROR ")
        #     return "Your entry is not correct"
        data = db_data.get_sequence_by_name(sequence_name)
        return data

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


api2.add_resource(SequenceData, '/sequence')
