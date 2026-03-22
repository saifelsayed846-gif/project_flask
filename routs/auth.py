from flask import Blueprint,render_template,redirect,request,session
from werkzeug.security import check_password_hash
import sqlite3

auth=Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        name=request.form['name']
        password=request.form['password']

        db=sqlite3.connect('database.db')
        cr=db.cursor()
        cr.execute('select * from users where name =?',(name,))
        user=cr.fetchone()
        db.close()    
        if user and check_password_hash(user[3],password):
            session['user']=user[0]
            
            return redirect('/')

    return render_template('login.html')  
@auth.route('/logout')
def loguou():
    session.clear()
    return redirect('/login')  