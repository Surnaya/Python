import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
m = Matrix(list1)
n = Matrix(list2)
print(f'Матрица: \n{m}')
print(f'Новая матрица: \n{m + n}')
