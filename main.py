from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_socketio import SocketIO

id = 1
objects = []

class user:
    def __init__(self, username, admin_status):
        global id
        self.admin = admin_status
        self.user_id = id
        id = id + 1
        self.username = username

        def test():
            print("Works~!")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_CHOICE = str(request.form['choice'])
    print("Welcome ", POST_USERNAME, POST_CHOICE, "~")
    result = 1
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return sessions(POST_USERNAME, POST_CHOICE)

@app.route('/sessions')
def sessions(username, session_type):
    if session_type == "create":
        admin_status = True
        user_object = user(username, admin_status)
        objects.append(user_object)
        return render_template('session.html', username=username)
    else:
        admin_status = False
        user_object = user(username, admin_status)
        objects.append(user_object)
        return "Something else.."

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print("Number of users=", len(objects))
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
