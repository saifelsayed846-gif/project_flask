from flask import Flask,render_template
from routs.crud import crud
from routs.auth import auth
from db import create,get_db

create()

app=Flask(__name__)
app.config.from_object('config')

@app.errorhandler(404)
def dontfound(y):
    return render_template('404.html')
@app.errorhandler(403)
def dontfound(y):
    return render_template('403.html')

app.register_blueprint(crud)
app.register_blueprint(auth)
