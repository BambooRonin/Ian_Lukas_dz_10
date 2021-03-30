a = [[9, 1, 5, 7], [2, 5, 2, 3], [5, 3, 8, 8]]
b = [[4, 7, 6, 1], [2, 9, 5, 8], [1, 7, 2, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1\n{matrix_1}\n{"-" * 20}')
print(f'Matrix 2\n{matrix_2}\n{"-" * 20}')
print(f'Matrix 1 + Matrix 2\n{matrix_1 + matrix_2}')
