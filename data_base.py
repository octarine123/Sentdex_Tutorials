import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial_1.db')
#conn=connect to database

c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE stuffToPlot(ID INT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

idfordb = 4
keyword = 'Python Sentence'
value = 10
unix = int(time.time())
date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))

def DataEntry():
    
    c.execute("INSERT INTO stuffToPlot (ID, unix, datestamp,keyword, value) VALUES (?,?,?,?,?)",
        (idfordb, unix, date, keyword, value))
    
    conn.commit()
