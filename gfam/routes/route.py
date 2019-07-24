from flask import Blueprint, jsonify, request
from flask_restplus import Resource, Api, reqparse
from gfam.services import service

mod = Blueprint('api', __name__)
api = Api(mod)


@api.route('/gfam')
class GeneFamily(Resource):
    def get(self):
        args = request.args #.get('gfam_id')
        # parse = reqparse.RequestParser()
        # parse.add_argument('gfam_id')
        # parse.add_argument('id', type=int)
        # args = parse.parse_args()
        #
        # {
        #     "message": {
        #         "id": "Invalid ID"
        #     }
        # }
        if 'gfam_id' in args:
            return service.fetch_by_gfamid(args['gfam_id'])
        if 'id' in args:
            return service.fetch_by_id(args['id'])
        else:
            data = service.fetch_all_data()
            return jsonify(data)

    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass