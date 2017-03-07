from models.users import User
from flask import Blueprint, render_template, redirect, url_for

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


@users_ctrl.route('/users/edit/<user_id>')
def user_edit(user_id):
    if not user_id.isnumeric():
        return redirect('/')
    return render_template('add_edit_person_form.html', user_id=user_id)


@users_ctrl.route('/users/remove/<user_id>')
def user_remove(user_id):
    User.remove_user(user_id)
    return redirect('/users')

