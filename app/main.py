from flask import Flask
from flask_socketio import SocketIO



app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY!!'
socketio = SocketIO(app, async_mode=None)

from .routes import *
from .socketio import *




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
