# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3

# connection = sqlite3.connect('teatchers.db') 
# cursor = connection.cursor() 
# sqlquery = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY
# );"""
# cursor.execute(sqlquery) 
# connection.commit()
# connection.close() 

# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# sqlquery = """INSERT INTO Students (
#   Student_Id , Student_Name , School_Id )
# VALUES ('201', 'Иван', '1'),
# ('202', 'Петр ', '2'), 
# ('203', 'Анастасия', '3'), 
# ('204', 'Игорь', '4');"""
# cursor.execute(sqlquery) 
# connection.commit()
# connection.close()

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_detail(student_id):
  try:
    connection = get_connection() 
    cursor = connection.cursor() 
    select_query = ''' SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name from Students JOIN School ON Students.School_Id = School.School_Id WHERE student_id = ?;'''
    cursor.execute(select_query, (student_id,))
    record = cursor.fetchone()
    close_connection(connection)
    print("Данные по студенту:", student_id)
    print("ID cтудента", record[0])
    print("Имя студента", record[1])
    print("ID школы",record[2])
    print("Название школы",record[3])
  except (Exception, sqlite3.Error) as error: # если бы была ошибка то вывели бы его
    print('Ошибка в получении данных:', error)

x = int(input("ВВеди ID студента:"))
get_student_detail(x)