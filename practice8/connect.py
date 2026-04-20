import sqlite3
from config import dbname
def connect_db():
    return sqlite3.connect(dbname)