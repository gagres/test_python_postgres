import psycopg2 as p
import os

host = os.environ['SERVER_PORT_5432_TCP_ADDR']
port = os.environ['SERVER_PORT_5432_TCP_PORT']
dbname = os.environ['SERVER_ENV_POSTGRES_DB']
dbuser = os.environ['SERVER_ENV_POSTGRES_USER']
dbpass = 'admin'

con = p.connect("host='%s' port='%s' dbname='%s' user='%s' password='%s'" % 
      (host, port, dbname, dbuser, dbpass))
cur = con.cursor()

def selectAll():
    cur.execute("SELECT * FROM Persons")
    return cur.fetchall()

def addNew(personId, personName):
    cur.execute("INSERT INTO Persons VALUES (%s, %s);", (personId, personName))
    con.commit()
    return selectAll()