import sqlite3

def connect():
    conn = sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, number INTEGER)")
    conn.commit()
    conn.close()


def insert(title,author,year,number):
    conn = sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,number))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows= cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",number=""):
    conn = sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book where title = ? OR author = ? OR year = ? OR number = ?", (title,author,year,number))
    rows= cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,number):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, number=? WHERE id=?",(title,author,year,number,id))
    conn.commit()
    conn.close()



connect()
#insert("The old man and the sea","Ernest Hemingway",1952,12345)
#print(view())
