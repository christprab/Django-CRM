#install MySQL to computer
#pip install mysql-connector-python and the default


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'christprab',
    password = 'Ch@rmander1091'
    )

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a db
cursorObject.execute("CREATE DATABASE countryco")

print("Already setup DB")

