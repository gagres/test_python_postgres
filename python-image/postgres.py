import psycopg2 as p

con = p.connect("dbname='admin' user='admin' password='admin' host='172.17.0.2' port='5432'")
cur = con.cursor()

def selectAll():
    cur.execute("SELECT * FROM Persons")
    return cur.fetchall()

def addNew(personId, personName):
    cur.execute("INSERT INTO Persons VALUES (%s, %s);", (personId, personName))
    return selectAll()