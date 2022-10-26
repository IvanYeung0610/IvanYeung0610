# Ivan Yeung Daniel Yentin
# SoftDev
# K18 -- (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-25
# time spent: 1

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
    courses = csv.DictReader(courses)
    c.execute("create table courses(code text, mark int, id int)")

    for row in courses:
        code = row['code']
        mark = row['mark']
        id = row['id']

        c.execute(f"insert into courses values('{code}', {mark}, {id})")
#==========================================================

db.commit() #save changes
db.close()  #close database
