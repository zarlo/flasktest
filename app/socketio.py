import html
from .main import socketio, session
from flask_socketio import emit, disconnect
import sys
from .chatlog import *
import markdown2

# this is not used yet


@socketio.on('join', namespace='/chat')
def chat_join(name):
    session['Name'] = html.escape(name)
    sendToChat(session['Name'] + " Joined")


@socketio.on('chat', namespace='/chat')
def chat_message(message):
    data = markdown2.markdown(html.escape(message))
    chatlog.AddChatLog(session['Name'], data)
    sendToChat(session['Name'] + ":" + data)


@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    sendToChat(session['Name'] + ' Left')
    session['Name'] = None


def sendToChat(msg):
    print('Chat>>' + msg)
    emit('chat', msg, broadcast=True)
