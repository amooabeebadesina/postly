from flask import jsonify

class JSONResponse:

    @staticmethod
    def sendSuccessResponse(data, statusCode=200):
        response = {
            'status': 'success',
            'data': data
        }
        return jsonify(response), statusCode

    @staticmethod
    def sendErrorResponse(msg, statusCode=200):
        response = {
            'status': 'error',
            'msg': msg,
            'data': None
        }
        return jsonify(response), statusCode
