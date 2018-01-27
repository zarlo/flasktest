from flask import Flask, session
from flask_socketio import SocketIO


from .chatlog import *
from .mem import *


chatlog.Init(mem.AddChatLog, mem.Getlast20)

chatlog.AddChatLog('test', 'this is a test')

app = Flask(__name__)


app.secret_key = 'SECRET_KEY!!'
socketio = SocketIO(app, async_mode=None)

from .routes import *
from .socketio import *

socketio.run(app, host='0.0.0.0')
