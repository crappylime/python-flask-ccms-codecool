from functools import wraps
from flask import flash, session, redirect, url_for


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

def permission(permission_list):
    def real_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if session['user_role'] in permission_list:
                return f(*args, **kwargs)
            else:
                flash('Access denied.')
                return redirect('/')
        return wrapper
    return real_decorator
