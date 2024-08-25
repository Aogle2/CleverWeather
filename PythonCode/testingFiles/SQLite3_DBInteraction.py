import sqlite3 as s3
import os

#working on the functions and stuff.
def setdb():
    database = s3.connect(os.path.join(os.getcwd(), "StarterDB.sqlite"))
    print(database.total_changes)


setdb()