from flask import render_template,request,redirect,flash,Blueprint,session,abort
from db import insert,show,delete,update
from werkzeug.security import generate_password_hash 
import sqlite3

crud=Blueprint('crud',__name__)
@crud.route('/',methods=['GET','POST'])
def saif():
    if request.method=='POST':
        name=request.form.get('name')
        jop=request.form.get('jop')
        password=request.form.get('password')
        password_hashing=generate_password_hash(password)
        if not name or not jop or not password:
            flash('enter all the database please')
        else:

            insert(name,jop,password_hashing)
            flash('added successfully')
                
            
    users=show()        
    return render_template('form.html',users=users)           
@crud.route('/dele/<int:user_id>')
def delet(user_id):
    if 'user' not in session:
        abort(403)
    delete(user_id)
    flash('deleted succussfully')
    return redirect('/')

@crud.route('/update/<int:user_id>',methods=['GET','POST'])
def up(user_id):
    if 'user' not in session:
        abort(403)
    db=sqlite3.connect('database.db')
    cr=db.cursor()
    cr.execute('select * from users where id=?',(user_id,))
    user=cr.fetchone()
    if request.method=='POST':
        new_name=request.form.get('new_name')   
        new_jop=request.form.get('new_jop')   
        new_password=request.form.get('new_password')
        new_password_hashing=generate_password_hash(new_password)

        update(new_name,new_jop,new_password_hashing,user_id) 
        flash('updated successfully')

    return render_template('update.html',user=user)


          

        