from flask import Flask, Blueprint
from flask_restful import Api

from pusher.utils import apply_middleware
from config import APP_CONFIG


def create_app():
    app = Flask(__name__)
    app.secret_key = APP_CONFIG.SECRET_KEY
    app.config.from_object(APP_CONFIG)
    apply_middleware(app)
    return app


def create_api(app):
    from pusher.modules.views import (Preparation, Login, Wallet, )

    api_bp = Blueprint('api_v1', __name__, url_prefix=f'{APP_CONFIG.API_URL_PREFIX}/v1')
    api = Api(app=api_bp)
    api.add_resource(Preparation, '/pusher/<link>')
    api.add_resource(Login, '/login')
    api.add_resource(Wallet, '/register')
    app.register_blueprint(api_bp)
    return api
