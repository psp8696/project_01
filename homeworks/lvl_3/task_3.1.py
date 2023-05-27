# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)
from pprint import pprint

class Matrix:

    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.matrix = [[n for j in range(x)] for i in range(y)]

    def print_m(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])
    
    def count(self):
        matrix=self.matrix
        x = len(matrix)
        for sublist in matrix:
            y = len(sublist)
        print("Число строк:", x, "число колонок:", y)

    def new_value(self, value):
        self.value = value
        matrix = self.matrix
        for index, item in enumerate(matrix):
            item = self.value
            matrix = [[index for item in range(len(matrix))] for item in range(len(matrix))]
        pprint(matrix)

       

m = Matrix(10, 10, 1)
m.print_m()
m.count()
m.new_value(9)