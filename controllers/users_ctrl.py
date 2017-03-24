from models.users import User
from models.assignments import Assignment
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from models.menus import Menu
from functools import wraps

users_ctrl = Blueprint('users_ctrl', __name__)
mainmenu = Menu.get_main_menu()


def permission_check(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        function_name = __name__.split('.')[-1] + '.' + f.__name__
        if session['user_role'] in Menu.get_menu_by_name(function_name).permissions:
            return f(*args, **kwargs)
        else:
            flash('Access denied.')
            return redirect(url_for('index'))

    return wrap


@users_ctrl.route('/users')
def users_list():
    users = User.get_user_list()
    return render_template('users.html', users=enumerate(users), role=None)


@users_ctrl.route('/users/<user_id>')
def user_details(user_id):
    if not user_id.isnumeric():
        flash("Site not found")
        return redirect('/')
    assignment_list = Assignment.get_assignment_list()
    return render_template('user_details.html', assignment_list=assignment_list, user=User.get_user_by_id(user_id),
                           mainmenu=mainmenu, dashboard=False)


@users_ctrl.route('/users/role=<role>')
def users_list_by_role(role):
    roles = ['mentor', 'student', 'boss', 'staff']
    if role not in roles:
        return redirect(url_for('users_ctrl.users_list'))
    users = User.get_user_list_by_role(role)
    return render_template('users.html', users=enumerate(users), role=role, mainmenu=mainmenu)


@users_ctrl.route('/users/new/<role>', methods=['GET', 'POST'])
def user_add(role):
    if request.method == "POST":
        name = request.form['firstname'] + ' ' + request.form['lastname']
        mail = request.form['email']
        temp_user = User.temporary_user(name, mail, role=role)
        if mail in User.get_mails_list():
            flash("E-mail address is already in use. Please provide another e-mail address")
            return render_template("add_edit_person_form.html", role=role, user=temp_user, fieldset_title="Add ",
                                   mainmenu=mainmenu)
        password = request.form['password']
        new_user = User.add_user(name, mail, password, role)
        flash('User {} has been added.'.format(new_user.name))
        return redirect(url_for('users_ctrl.users_list_by_role', role=role))
    return render_template("add_edit_person_form.html", role=role, fieldset_title="Add ", user=None, mainmenu=mainmenu)


@users_ctrl.route('/users/edit/<user_id>', methods=['GET', 'POST'])
def user_edit(user_id):
    if not user_id.isnumeric():
        flash("Site not found")
        return redirect('/')
    if request.method == "POST":
        user_to_edit = User.get_user_by_id(user_id)
        new_name = request.form['firstname'] + ' ' + request.form['lastname']
        user_to_edit.set_name(new_name)
        new_mail = request.form['email']
        if new_mail != user_to_edit.mail and new_mail in User.get_mails_list():
            flash("E-mail address is already in use. Please provide another e-mail address")
            return render_template("add_edit_person_form.html", user=user_to_edit, fieldset_title="Edit ", role=None,
                                   mainmenu=mainmenu)
        new_password = request.form['password']
        user_to_edit.set_mail(new_mail)
        user_to_edit.set_password(new_password)
        user_to_edit.save_changes()
        flash(user_to_edit.name + ' data has been edited')
        return redirect(url_for('users_ctrl.users_list_by_role', role=user_to_edit.get_user_class_name()))
    return render_template('add_edit_person_form.html', user=User.get_user_by_id(user_id), fieldset_title="Edit ",
                           role=None, mainmenu=mainmenu)


@users_ctrl.route('/users/remove/<user_id>')
def user_remove(user_id):
    user_to_remove = User.get_user_by_id(user_id)
    user_to_remove.remove()
    flash("{} {} has been removed".format(user_to_remove.get_user_class_name(), user_to_remove.name))
    return redirect(url_for('users_ctrl.users_list_by_role', role=user_to_remove.get_user_class_name().lower()))
