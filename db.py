import sqlite3
def get_db():
    return sqlite3.connect('database.db')

def create():
    db=get_db()
    cr=db.cursor()
    cr.execute('create table if not exists users (id integer primary key autoincrement,name,jop,password)')
    db.commit()
    db.close()

def insert(name,jop,password):
    db=get_db()
    cr=db.cursor()
    cr.execute('insert into users(name,jop,password) values(?,?,?)',(name,jop,password))
    db.commit()
    db.close()

def show():
    db=get_db()
    cr=db.cursor()
    cr.execute('select * from users')
    return cr.fetchall()
    
def delete(user_id):
    db=get_db()
    cr=db.cursor()
    cr.execute('delete from users where id=?',(user_id,))
    db.commit()
    db.close()

def update(name,jop,password,user_id):
    db=get_db()
    cr=db.cursor()
    cr.execute('update users set name=?,jop=?,password=? where id=?',(name,jop,password,user_id))
    db.commit()
    db.close()        


