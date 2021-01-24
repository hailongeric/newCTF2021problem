from flask import render_template, redirect, url_for, request, flash, session as flask_session, Flask
from flask_bootstrap import Bootstrap

from config import Config
from models import init_sessionmaker, session_scope

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from forms import CreateNoteForm

init_sessionmaker()

import string
import random
import time
import datetime


def get_random_id():
    alphabet = list(string.ascii_lowercase + string.digits)
    return ''.join([random.choice(alphabet) for _ in range(32)])


@app.route('/')
@app.route('/index')
def index():
    with session_scope() as session:
        cursor = session.execute("SELECT title, text, note_id FROM notes WHERE prv = 'False'").cursor
        posts = cursor.fetchall()
    return render_template('index.html', posts=posts)


@app.route('/logout')
def logout():
    flask_session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    try:
        form = CreateNoteForm()
        if request.method == "POST":
            with session_scope() as session:
                username = form.username.data
                
                title = form.title.data
                body = form.body.data
                prv = str(form.private.data)
                
                cursor = session.execute("SELECT user_id FROM users WHERE username = :username",
                                         {'username': username, }).cursor
                c = cursor.rowcount
                if c > 0:
                    user_id = cursor.fetchone()[0]
                    
                    timestamp = round(time.time(), 4)
                
                    post_at = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
                    
                    random.seed(user_id + post_at)
                    note_id = get_random_id()
                    
                    session.execute(
                        '''INSERT INTO notes (user_id, note_id, text, title, post_at, prv) 
                        VALUES (:user_id,:note_id,:text,:title, :post_at, :prv)''',
                        {
                            'user_id': user_id, 'note_id': note_id, 'text': body,
                            'title': title, 'post_at': post_at, 'prv': prv
                        })

                    return redirect(url_for('index'))

                else:
                    timestamp = round(time.time(), 4)
                    
                    random.seed(timestamp)
                    user_id = get_random_id()
                    
                    session.execute('''INSERT INTO users (user_id, username) VALUES (:user_id, :username)''',
                                    {
                                        'user_id': user_id, 'username': username
                                    })
                    post_at = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
                    random.seed(user_id + post_at)
                    note_id = get_random_id()

                    session.execute(
                        '''INSERT INTO notes (user_id, note_id, text, title, post_at, prv) 
                        VALUES (:user_id,:note_id,:text,:title, :post_at, :prv)''',
                        {
                            'user_id': user_id, 'note_id': note_id, 'text': body,
                            'title': title, 'post_at': post_at, 'prv': prv
                        })
                    flask_session['username'] = username

                    return redirect(url_for('index'))
        else:
            return render_template("create.html", form=form)
    except Exception as e:
        return str(e)


@app.route('/my_notes')
def my_notes():
    with session_scope() as session:
        if (flask_session.get('username')):
            username = flask_session['username']
            cursor = session.execute("SELECT user_id FROM users WHERE username = :username",
                                     {'username': username}).cursor
            res = cursor.fetchall()
            if len(res) == 0:
                flask_session.pop('username', None)
                return redirect(url_for('index'))
            user_id = res[0]
        else:
            user_id = request.args.get('user_id')

        cursor = session.execute("SELECT title, text, note_id FROM notes WHERE user_id = :user_id",
                                 {'user_id': user_id}).cursor
        posts = cursor.fetchall()
        return render_template("my_notes.html", posts=posts)


@app.route('/view/<_id>')
def view(_id):
    with session_scope() as session:
        cursor = session.execute("SELECT post_at,title,text,user_id FROM notes WHERE note_id = :note_id",
                                 {'note_id': _id}).cursor
        res = cursor.fetchone()
        user_id = res[3]
        cursor = session.execute("SELECT username FROM users WHERE user_id = :user_id",
                                 {'user_id': user_id}).cursor
        username = cursor.fetchone()[0]

        data = {
            'post_at': res[0],
            'title': res[1],
            'text': res[2],
            'username': username
        }

        return render_template('note.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)