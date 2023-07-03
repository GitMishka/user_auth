from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


users = {'admin': generate_password_hash("admin")}

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form['username']
    if username in users and check_password_hash(users[username], request.form['password']):
        user = User()
        user.id = username
        login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'

@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + str(current_user.get_id())

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.run(debug=True)
