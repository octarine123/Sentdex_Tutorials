import sqlite3
import time
import datetime

conn = sqlite3.connect('tutorial_1.db')
c = conn.cursor()
sql = "SELECT * FROM stuffToPlot WHERE keyword =?"

wordUsed = 'Python Sentence'

def readData():
    for row in c.execute(sql, [(wordUsed)]):
        print(row)

readData()
