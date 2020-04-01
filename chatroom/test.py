import sqlite3

my_connerctio = sqlite3.connect("test.db")
my_cursor = my_connerctio.cursor()
# table_name = 'a'
# values = "id integer primary key autoincrement, age int, gender boolen, country varchar(256), status int"
# my_cursor.execute("create table {}({})".format(table_name, values))
# my_connerctio.commit()
# my_cursor.execute("create table member(id int, name varchar(256))")
# my_cursor.execute("insert into member (id, name) values (1, 'sara') ")
table_name = 'b'
values = "id integer primary key autoincrement, age int, gender ['f','m'], country varchar(256), status [0,1,2]"
# my_cursor.execute("create table {}({})".format(table_name, values))
a = "age, gender, country, status"
my_cursor.execute("insert into b ({}) values (12,'f','t',1)".format(a))
# my_connerctio.commit()
# result = my_cursor.execute("select id,age from b where country == 't'")
# print(result.fetchall()[0][1])

res = my_cursor.execute("select age, gender from b where gender = 'm'")
print(type(res.fetchall()))
# my_connerctio.commit()
# if my_cursor.fetchall() == []:
