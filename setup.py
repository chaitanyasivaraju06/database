import sqlite3

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()
try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('okra')")
cursor.execute("insert into list (description) values ('corn')")
cursor.execute("insert into list (description) values('beans')")
cursor.execute("insert into list (description) values ('carrot')")
cursor.execute("insert into list (description) values ('Tomatoes')")
connection.commit()
connection.close()