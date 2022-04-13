from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        type=str,
                        help="username Field Required")

    parser.add_argument('password',
                        required=True,
                        type=str,
                        help="password Field Required")

    def post(self, name):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'USer with this username is already exist'}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {'message': 'User Register successfully'}, 201
