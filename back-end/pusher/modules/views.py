from flask_restful import Resource
import secrets
from typing import Tuple
from pusher.db import DBEngine


class Preparation(Resource):
    def get(self, link) -> dict:
        return {'test': 1}

    def post(self):
        pass


class Login(Resource):
    def post(self) -> Tuple[dict, int]:
        # validation
        link_hash = secrets.token_hex(nbytes=64)
        user_hash = secrets.token_hex(nbytes=64)
        with DBEngine() as db_engine:
            db_engine.insert(table='sessions', data=[{'user': user_hash, 'path': link_hash}])

        return {'link': link_hash}, 200
