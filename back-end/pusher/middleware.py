from flask import abort
from pusher.db import DBEngine
from flask import request

from datetime import datetime, timedelta


def session_manager():
    if request.path in ('/api/v1/login', '/api/v1/register'):
        return None

    session_id = request.headers.get('X-Session-Id')
    session_path = request.headers.get('X-Session-Path')

    with DBEngine() as db_engine:
        data = db_engine.get(table='sessions',
                             query={'path': session_path,
                                    'session_id': session_id})
        if not data or \
           datetime(1970, 1, 1) + timedelta(
               milliseconds=data[0]['creation_date']['$date'], minutes=30
           ) < datetime.utcnow():
            abort(401)


MIDDLEWARE_LIST = (session_manager,)
