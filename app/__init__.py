from flask import Flask, request, send_from_directory, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=None)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

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




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
