from flask import Flask, render_template, request, session, redirect, g, url_for, Blueprint
from db_controller import DB
from controllers.assignments_ctrl import assignments_list

DATABASE = 'data/ccms.db'

app = Flask(__name__)
app.register_blueprint(assignments_list)


def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = DB.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db:
        db.close()


@app.route("/<what>")
def index():
    pass


if __name__ == "__main__":
    # DB.create_database()
    app.run(debug=True)


