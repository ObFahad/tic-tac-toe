from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_folder = './templates')
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode = None)


from app import routes
