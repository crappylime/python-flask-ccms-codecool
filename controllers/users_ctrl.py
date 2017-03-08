from models.users import User
from flask import Blueprint, render_template, redirect, url_for, request, flash

users_ctrl = Blueprint('users_ctrl', __name__)


@users_ctrl.route('/users')
def users_list():
    users = User.get_user_list()
    return render_template('users.html', users=enumerate(users), role=None)


@users_ctrl.route('/users/<user_id>')
def user_details(user_id):
    if not user_id.isnumeric():
        return redirect('/')
    return render_template(user_details, user_id=user_id)


@users_ctrl.route('/users/role=<role>')
def users_list_by_role(role):
    roles = ['mentor', 'student', 'boss', 'staff']
    if role not in roles:
        return redirect(url_for('users_ctrl.users_list'))
    users = User.get_user_list_by_role(role)
    return render_template('users.html', users=enumerate(users), role=role)


@users_ctrl.route('/users/new/<role>', methods=['GET', 'POST'])
def user_add(role):
    if request.method == "POST":
        name = request.form['firstname'] + ' ' + request.form['lastname']
        mail = request.form['email']
        if mail in User.get_mails_list():
            flash("E-mail address is already in use. Please provide another e-mail address")
            return render_template("add_edit_person_form.html", role=role, fieldset_title="Add ")
        password = request.form['password']
        User.add_user(name, mail, password, role)
        return redirect(url_for('users_ctrl.users_list_by_role', role=role))
    return render_template("add_edit_person_form.html", role=role, fieldset_title="Add ")


@users_ctrl.route('/users/edit/<user_id>')
def user_edit(user_id):
    if not user_id.isnumeric():
        return redirect('/')
    return render_template('add_edit_person_form.html', user_id=user_id)


@users_ctrl.route('/users/remove/<user_id>')
def user_remove(user_id):
    User.remove_user(user_id)
    return redirect('/users')

