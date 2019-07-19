from flask import Blueprint, jsonify, request, abort
from flask_restplus import Resource, Api, reqparse
from gfam.model.sequence_model import Sequence1
from gfam import db

mod1 = Blueprint('api2', __name__)
api2 = Api(mod1)

@api2.route('/sequence')
class SequenceData(Resource):
    """
    #Main class to get, post, delete, put sequence data
    """
    def get(self):
        data = Sequence1.query.all()
        output = []
        for i in data:
            sequence_data = {}
            sequence_data['id'] = i.id
            sequence_data['sequence_name'] = i.sequence_name
            sequence_data['sequence'] = i.sequence
            sequence_data['version'] = i.version
            output.append(sequence_data)
        return jsonify({'todos' : output})


    def post(self):
        def create_todo():
            data = request.get_json()
            new_todo = Todo(text=data['text'], complete=False, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()
            return jsonify({'message' : "Todo created!"})

    def put(self):
        pass

    def delete(self):
        pass

