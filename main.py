from flask import Flask, render_template, request, session, redirect, g, url_for, Blueprint, flash
from db_controller import DB
from models.users import User
from models.assignments import Assignment
from models.menus import Menu

from functools import wraps
import os

from controllers.users_ctrl import users_ctrl
from controllers.teams_ctrl import teams_ctrl
from controllers.attendances_ctrl import attendances_ctrl
from controllers.checkpoints_ctrl import checkpoints_ctrl
from controllers.submissions_ctrl import submissions_ctrl
from controllers.assignments_ctrl import assignments_ctrl

DATABASE = 'data/ccms.db'

app = Flask(__name__)

app.register_blueprint(attendances_ctrl)
app.register_blueprint(checkpoints_ctrl)
app.register_blueprint(submissions_ctrl)
app.register_blueprint(assignments_ctrl)
app.register_blueprint(users_ctrl)
app.register_blueprint(teams_ctrl)
app.secret_key = os.urandom(24)

mainmenu = Menu.get_main_menu()


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user_mail = request.form['email']
        if user_mail in User.get_mails_list():
            logged_user = list(filter(lambda x: x.get_mail() == user_mail, User.get_user_list()))[0]
            if request.form['password'] != logged_user.get_password():
                error = "Wrong password. Try again"
            else:
                session['logged_in'] = True
                session['user_id'] = logged_user.get_id()
                session['user_role'] = logged_user.get_user_class_name()
                session['user_name'] = logged_user.get_name()
                flash("You are logged in!")
                return redirect(url_for('index'))
        else:
            error = "No user with such email. Try again"
    return render_template('login.html', error=error)


@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash("You are logged out!")
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    if session['user_role'] == 'Student':
        assignment_list = Assignment.get_assignment_list()
    else:
        assignment_list = []
    return render_template('user_details.html', user=User.get_user_by_id(session['user_id']), assignment_list=assignment_list)


@app.route("/")
@login_required
def index():
    if session['user_role'] == 'Student':
        assignment_list = Assignment.get_assignment_list()
    else:
        assignment_list = []
    return render_template('user_details.html', user=User.get_user_by_id(session['user_id']), assignment_list=assignment_list, mainmenu=mainmenu)


if __name__ == "__main__":
    app.run(debug=True)
