#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"
#Opening the file from another machine does not neccesarily mean that it will work the same
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
# command = ""          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement

with open("students.csv", 'r') as students:
    db.execute("DROP TABLE if exists students") #semi colon at the end of command not required when using .execute command
    students = csv.DictReader(students)
    c.execute("create table students(name text, age int, id int)")

    for row in students:
        name = row['name']
        age = row['age']
        id = row['id']
    
        c.execute(f"insert into students values('{name}', {age}, {id})")
    #c.execute("select * from students")
    #c.fetchone()

with open("courses.csv", 'r') as courses:
    db.execute("DROP TABLE if exists courses")
    '''
    Came across error when trying to execute this command when opening a pre existing .db file.
    Was resolved by commenting out the c.execute("select * from students") inside previous with block
    ERROR:
        Traceback (most recent call last):
                File "/home/students/2023/iyeung30/Documents/Soft Dev/IvanYeung0610/18_csv2db/db_builder.py", line 36, in <module>
            db.execute("DROP TABLE if exists courses")
        sqlite3.OperationalError: database table is locked


    '''
    courses = csv.DictReader(courses)
    c.execute("create table courses(code text, mark int, id int)")

    for row in courses:
        code = row['code']
        mark = row['mark']
        id = row['id']
        
        c.execute(f"insert into courses values('{code}', {mark}, {id})")
c.execute("select * from students")
c.fetchall()
#==========================================================

db.commit() #save changes
db.close()  #close database


