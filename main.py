import mysql.connector
from config import user,password,host
try:
    connection=mysql.connector.connection(
        user=user,
        password=password,
        host=host
    )
    print("connected")
except:
    print("welllll")