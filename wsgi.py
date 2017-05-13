import os
import psycopg2

def dbconn():
    return psycopg2.connect(
        host =      os.getenv("POSTGRESQL_HOST", 'localhost'), 
        user =      os.getenv("POSTGRESQL_USER", 'admin'),
        password =  os.getenv("POSTGRESQL_PASSWORD", ''),
        dbname =    os.getenv("POSTGRESQL_DATABASE", 'sampledb')
    )

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    conn = dbconn()
    print(conn)
    cur = conn.cursor()
    cur.execute("SELECT * FROM systems_populated")
    rows = cur.fetchall()
    print(rows)
    conn.close
    return "Hello World! :-) First value: {}, Second Value: {}".format(rows[0][0], rows[1][0])

if __name__ == "__main__":
    application.run()
    