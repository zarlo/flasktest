
from .main import socketio, session
from flask_socketio import  emit, disconnect
import sys

@socketio.on('join', namespace='/chat')
def chat_join(name):
    session['Name'] = name
    sendToChat(session['Name'] + " Joined")

@socketio.on('chat', namespace='/chat')
def chat_message(message):
    sendToChat(session['Name'] + ":" + message)


@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    try:
        sendToChat(session['Name'] + ' Left')
    except Exception as e:
        raise

    session['Name'] = None

def sendToChat(msg):
    print('Chat>>' + msg)
    emit('chat', msg)
