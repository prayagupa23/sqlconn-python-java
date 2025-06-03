# to connect MS SQL database using pyodbc
import pyodbc as odbc

DRIVER_NAME= ''
SERVER_NAME = ''
DATABASE_NAME = ''
USER_ID = ''
PASSWORD= ''

connection_string = f"""
DRIVER= {{{DRIVER_NAME}}};
SERVER = {SERVER_NAME};
DATABASE = {DATABASE_NAME};
trust_connection = yes;
UID = {USER_ID};
PID = {PASSWORD};
"""

conn = odbc.connect(connection_string)
sql_query = """
SELECT @@SERVERNAME
"""

cursor = conn.cursor()
cursor.execute(sql_query)