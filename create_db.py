import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ism.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE users(uid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,phone text,dob text,dor text,pass text,utype text,address text,fees text)")
    con.commit()

create_db()