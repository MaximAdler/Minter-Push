import os

from config import APP_CONFIG
from pusher import app

if os.environ.get('STANDALONE') is None:
    os.environ['STANDALONE'] = 'true'
os.environ['FLASK_ENV'] = 'development'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=APP_CONFIG.APP_PORT)
