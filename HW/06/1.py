class Matrix:
    def __init__(self, n, m):
        self.matrix = self.get_matrix(n, m)

    def get_matrix(self, n, m):
        num = 1
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = num
                num += 1
        return matrix

    def get_readable_matrix_string(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.get_readable_matrix_string(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def getElement(self, i, j):
        return self.matrix[i-1][j-1]

    def setElement(self, i, j, element):
        self.matrix[i-1][j-1] = element

    def transpose(self, matrix):
        return [list(i) for i in zip(*matrix)]

    def getTranspose(self):
        return self.get_readable_matrix_string(self.transpose(self.matrix))

    def doTranspose(self):
        self.matrix = self.transpose(self.matrix)

    def multiply(self, matrix):
        result = [[0 for j in range(len(matrix[i]))]
                  for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(matrix[0])):
                for k in range(len(matrix)):
                    result[i][j] += self.matrix[i][k] * matrix[k][j]
        return result

    def getMultiply(self, matrix):
        return self.get_readable_matrix_string(self.multiply(matrix))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.get_readable_matrix_string(self.multiply(other))
        return self.get_readable_matrix_string([[num*other for num in row] for row in self.matrix])


class Square_matrix(Matrix):
    def __init__(self, n, m,):
        super().__init__(n, m)


f = Square_matrix(5, 5)
print(f)


# m1 = Matrix(2, 3)
# print(m1)
# # [1, 2, 3]
# # [4, 5, 6]
# print(m1.getElement(2,2))
# # 5
# m1.setElement(2,2,-10)
# print(m1.getTranspose())
# # [1, 4]
# # [2, -10]
# # [3, 6]
# print(m1)
# # [1, 2, 3]
# # [4, -10, 6]
# m1.doTranspose()
# print(m1)
# # [1, 4]
# # [2, -10]
# # [3, 6]
# m2 = Matrix(2,3)
# print(m2)
# # [1, 2, 3]
# # [4, 5, 6]
# print(m2.getMultiply(m1))
# # [14, 2]
# # [32, 2]
# print(m2 * m1)
# # [14, 2]
# # [32, 2]
# print(m1)
# # [1, 4]
# # [2, -10]
# # [3, 6]
# print(m1 * 3)
# # [3, 12]
# # [6, -30]
# # [9, 18]