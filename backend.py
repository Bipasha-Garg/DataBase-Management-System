import sqlite3
import os

def connect():
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data1 (id INTEGER PRIMARY KEY, fn TEXT, ln TEXT, term INTEGER, gpa REAL)")
    conn.commit()
    conn.close()

def insert(fn,ln,term,gpa):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data1 Values (NULL,?,?,?,?)", (fn,ln,term,gpa))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data1")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(fn="",ln="",term="",gpa=""):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute(
        "Select * FROM data1 WHERE fn=? or ln=? or term=? or gpa=?", (fn, ln, term, gpa)
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM data1 WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,fn,ln,term,gpa):
    conn = sqlite3.connect("Students.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE data1 SET fn=?, ln=?, term=?, gpa=? WHERE id=?", (fn, ln, term, gpa, id)
    )
    conn.commit()
    conn.close()

def delete_data():
    if os.path.exists("Students.db"):
        os.remove("Students.db")
    connect()

connect()
