from models.users import User
from models.assignments import Assignment
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, json
from models.menus import Menu
from common import login_required, permission


users_ctrl = Blueprint('users_ctrl', __name__)
mainmenu = Menu.get_main_menu()



@users_ctrl.route('/users')
@permission(["Student", "Mentor"])
@login_required
def users_list():
    users = User.get_user_list()
    return render_template('users.html', users=enumerate(users), role=None)


@users_ctrl.route('/users/<user_id>')
@permission(["Student", "Mentor", "Boss"])
@login_required
def user_details(user_id):
    if not user_id.isnumeric():
        flash("Site not found")
        return redirect('/')
    assignment_list = Assignment.get_assignment_list()
    return render_template('user_details.html', assignment_list=assignment_list, user=User.get_user_by_id(user_id), mainmenu=mainmenu, dashboard=False)


@users_ctrl.route('/users/role=<role>')
@login_required
def users_list_by_role(role):
    roles = {'mentor': ['Mentor', 'User', 'Boss', 'Staff', 'Student'],
             'student': ['Mentor', 'User', 'Boss', 'Staff', 'Student'],
             'boss': ['Mentor', 'User', 'Boss', 'Staff'],
             'staff': ['Mentor', 'User', 'Boss', 'Staff']}
    if role not in roles:
        return redirect(url_for('users_ctrl.users_list'))
    if session["user_role"] not in roles[role]:
        flash('Access denied.')
        return redirect('/')
    users = User.get_user_list_by_role(role)
    return render_template('users.html', users=enumerate(users), role=role, mainmenu=mainmenu)


@users_ctrl.route('/users/new/<role>', methods=['POST'])
@login_required
def user_add(role):
    if request.method == "POST":
        name = request.form['firstname'] + ' ' + request.form['lastname']
        mail = request.form['email']
        temp_user = User.temporary_user(name, mail, role=role)
        if mail in User.get_mails_list():
            flash("E-mail address is already in use. Please provide another e-mail address")
            return render_template("add_edit_person_form.html", role=role, user=temp_user, fieldset_title="Add ", mainmenu=mainmenu)
        password = request.form['password']
        new_user = User.add_user(name, mail, password, role)
        flash('User {} has been added.'.format(new_user.name))
        return redirect(url_for('users_ctrl.users_list_by_role', role=role))
    return render_template("add_edit_person_form.html", role=role, fieldset_title="Add ", user=None, mainmenu=mainmenu)


@users_ctrl.route('/users/edit/<user_id>', methods=['GET', 'POST'])
@permission(['Mentor', 'Boss'])
@login_required
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
            return render_template("add_edit_person_form.html", user=user_to_edit, fieldset_title="Edit ", role=None, mainmenu=mainmenu)
        new_password = request.form['password']
        user_to_edit.set_mail(new_mail)
        user_to_edit.set_password(new_password)
        user_to_edit.save_changes()
        flash(user_to_edit.name + ' data has been edited')
        return redirect(url_for('users_ctrl.users_list_by_role', role=user_to_edit.get_user_class_name()))
    return render_template('add_edit_person_form.html', user=User.get_user_by_id(user_id), fieldset_title="Edit ", role=None, mainmenu=mainmenu)


@users_ctrl.route('/users/remove', methods=["POST"])
@login_required
def user_remove():
    user_id = request.get_json()
    user_to_remove = User.get_user_by_id(user_id)
    user_to_remove.remove()
    flash("{} {} has been removed".format(user_to_remove.get_user_class_name(), user_to_remove.name))
    return ''


@users_ctrl.route("/new_user", methods=["GET", "POST"])
def new_user():
    user_content = request.get_json()
    print(user_content)

    firstname = user_content["firstname"]
    lastname = user_content["lastname"]
    email = user_content["email"]
    if User.is_user_with_email_in_user_list(email):
        return "email taken"
    password = user_content["password"]
    role = user_content["role"]
    new_user = User.add_user(firstname+' '+lastname, email, password, role)
    new_user_in_json = json.dumps(new_user.__dict__, ensure_ascii=False)

    print(new_user_in_json)

    return new_user_in_json


@users_ctrl.route("/edit_user", methods=["GET", "POST"])
def edit_user():
    user_content = request.get_json()
    print(user_content)
    user_id = user_content['id']
    firstname = user_content["firstname"]
    lastname = user_content["lastname"]
    email = user_content["email"]
    if User.is_user_with_email_in_user_list(email):
        return "email taken"
    password = user_content["password"]

    user_to_edit = User.get_user_by_id(user_id)
    user_to_edit.set_name(firstname+' '+lastname)
    user_to_edit.set_mail(email)
    user_to_edit.set_password(password)
    user_to_edit.save_changes()

    edited_user_in_json = json.dumps(user_to_edit.__dict__, ensure_ascii=False)



    return edited_user_in_json

@users_ctrl.route("/get_user_by_id", methods=["GET", "POST"])
def get_user_by_id():

    user_id = request.get_json()

    user = User.get_user_by_id(user_id)
    user_in_json = json.dumps(user.__dict__, ensure_ascii=False)
    print(user_in_json)

    return user_in_json
