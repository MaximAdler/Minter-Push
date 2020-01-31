from flask_restful import Resource


class LinkGenerator(Resource):
    def get(self):
        return {'test': 1}

    def post(self):
        pass
