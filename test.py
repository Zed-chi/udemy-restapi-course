import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()
create_table = "create table users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, "bob", "qwe")
insert = "insert into users values (?,?,?)"
cursor.execute(insert, user)
users = [
    (2, "nob", "qwe"),
    (3, "xob", "qwe")
]
cursor.executemany(insert, users)

select = "select * from users"

cursor.execute(select)
con.commit()
con.close()