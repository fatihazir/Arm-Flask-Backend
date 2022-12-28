from flask import Flask, request
from flask_restful import Resource, Api
from results import SuccessResult, ErrorResult
from Apriori.apyori import apriori
from armProvider import RunApriori
from checkIncomingPostData import CheckIncomingPostDataIsValid
from messages import AliveMessage, BodyDataError, SuccessMessage, SystematicError
from werkzeug.exceptions import HTTPException, NotFound

app = Flask(__name__)
api = Api(app)


class ArmManager(Resource):
    def get(self):
        return SuccessResult({}, AliveMessage)

    def post(self):
        data = request.json
        minSupport = data['minSupport']
        maxLength = data['maxLength']
        minLength = data['minLength']
        elementAmount = data['elementAmount']
        userId = data['userId']
        alias = data['alias']
        data = data['data']

        if not CheckIncomingPostDataIsValid(data, minSupport, maxLength, minLength, elementAmount, userId, alias):
            return ErrorResult(BodyDataError)

        try:
            return SuccessResult(RunApriori(data, minSupport, maxLength, minLength, elementAmount, userId, alias), SuccessMessage)
        except:
            return ErrorResult(SystematicError)


api.add_resource(ArmManager, '/')


if __name__ == '__main__':
    app.run(debug=True)
