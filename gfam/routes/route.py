import json
from flask import Blueprint, jsonify, request, abort
from gfam.services import sequences
from flask_restful import Resource, Api, reqparse

mod = Blueprint('api', __name__)
api = Api(mod)


class SequenceData(Resource):
    """
    #Main class to get, post, delete, put sequence data
    """
    def get(self):
        return jsonify(sequences.load_data())

    def post(self):
        if not request.json or not 'sequence_name' in request.json:
            abort(400)
        sequence_data = sequences.load_data()
        item = {
                'sequence_id': sequence_data[-1]['sequence_id'] + 1,
                'sequence_name': request.json['sequence_name'],
                'sequence': request.json.get('sequence'),
                'version': request.json.get('version')
                }
        sequence_data.append(item)
        sequences.create_sequence(sequence_data)
        return jsonify({'Sequence': item})

    def put(self):
        pass

    def delete(self):
        query_string = request.args.get('sequence_id')
        return sequences.del_sequence(int(query_string))


api.add_resource(SequenceData, '/sequence')

# parser = reqparse.RequestParser()
# parser.add_argument('sequences_id', type=int)
# parser.parse_args()




















#
# @mod.route('/sequences')
# def index():
#     return jsonify(sequences.load_data())
#
#
# @mod.route('/sequences/<int:sequence_id>')
# def get_withsid(sequence_id):
#     return jsonify(sequences.get_sequence(sequence_id))
#
#
# @mod.route('/sequences/', methods=['POST'])
# def add_sequence():
#     if request.method == 'POST':
#         if not request.json or not 'sequence_name' in request.json:
#             abort(400)
#         sequence_data = sequences.load_data()
#         item = {
#             'sequence_id': sequence_data[-1]['sequence_id'] + 1,
#             'sequence_name': request.json['sequence_name'],
#             'sequence': request.json.get('sequence'),
#             'version': request.json.get('version')
#                }
#         sequence_data.append(item)
#         sequences.create_sequence(sequence_data)
#         return jsonify({'Sequence': item})



