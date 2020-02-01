from flask_restful import Resource
import secrets
from typing import Tuple
from pusher.db import DBEngine
from mintersdk.sdk.check import MinterCheck
from mintersdk.sdk.wallet import MinterWallet
from datetime import datetime

from flask import request, abort


class Preparation(Resource):
    def get(self, link) -> Tuple[dict, int]:
        return {'test': 1}, 200


class Wallet(Resource):
    def post(self) -> Tuple[dict, int]:
        mnemonic = request.json.get('mnemonic')
        wallet = MinterWallet.create(mnemonic=mnemonic)
        proof = MinterCheck.proof(
            address=wallet['address'],
            passphrase='mnemonic')

        with DBEngine() as db_engine:
            db_engine.insert(
                table='wallets',
                data=[{
                    'verification_id': 1
                 }])


class Login(Resource):
    def post(self) -> Tuple[dict, int]:
        address = request.json.get('address')
        passphrase = request.json.get('passphrase')
        link_hash = request.json.get('link')
        proof = MinterCheck.proof(
            address=address,
            passphrase=passphrase)

        with DBEngine() as db_engine:
            if not db_engine.get(
                table='wallets',
                query={'verification_id': proof}
            ):
                abort(401)

            if link_hash:
                if not db_engine.get(
                    table='links',
                    query={'link_hash': link_hash}
                ):
                    abort(401)
            else:
                link_hash = secrets.token_hex(nbytes=64)

            session_id = secrets.token_hex(nbytes=54)

            db_engine.insert(table='sessions', data=[{
                'path': link_hash,
                'creation_date': datetime.utcnow(),
                'session_id': session_id
            }])

        return {'lid': link_hash, 'sid': session_id}, 200
