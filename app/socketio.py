
from .main import socketio
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

@socketio.on('join')
def chat_join(name):
    if session['Name'] is not None:
        return
    session['Name'] = name
    emit('chat',
         {'data': 'Joined','name': session['Name']})

@socketio.on('chat')
def chat_message(message):
    emit('chat',
         {'data': ":" + message['data'], 'name': session['Name']})

@socketio.on('disconnect')
def test_disconnect():
        emit('chat',
             {'data': 'Left', 'name': session['Name']})
        session['Name'] = None
