from flask import Flask, session
from flask_socketio import SocketIO

print(__name__)

app = Flask(__name__)


app.secret_key = 'SECRET_KEY!!'
socketio = SocketIO(app, async_mode=None)

from .routes import *
from .socketio import *

socketio.run(app, host='0.0.0.0')
