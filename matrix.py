from copy import deepcopy


class MatrixValueError(Exception):
    _error = "Initialization argument must be a list (a list of lists)"


class AdditionValueError(Exception):
    _error = "Unknown right operand for operator +"


class AdditionSizeError(Exception):
    _error = "Matrices' sizes do not match for operator +"


class MultiplicationValueError(Exception):
    _error = "Unknown right operand for operator *"


class MultiplicationSizeError(Exception):
    _error = "Matrices' sizes do not match for operator *"


class Matrix:
    def __init__(self, given_matrix):
        try:
            if not isinstance(given_matrix, list):
                raise MatrixValueError
            self._matrix = deepcopy(given_matrix)
            self._sizes = list()
            self._depth = self.__depth__(self._matrix)
            level = self._matrix
            for i in range(self._depth):
                self._sizes.append(len(level))
                level = level[0]
            max_level = 4
            for i in range(self._depth, max_level):
                self._sizes.append(0)
            if self._sizes[1] == 0:
                self._matrix = [self._matrix]
                self._sizes[1] = self._sizes[0]
                self._sizes[0] = 1
        except MatrixValueError:
            print(MatrixValueError._error)

    def __str__(self):
        return str(self._matrix)

    def __depth__(self, lst):
        return 1 + self.__depth__(lst[0]) if isinstance(lst, list) else 0

    def __size__(self):
        return tuple(self._sizes)

    size = property(__size__)

    def __slice__(self, slice_one, slice_two=None, slice_three=None, slice_four=None):
        result = self._matrix[slice_one]
        if slice_two is not None:
            result = [line[slice_two] for line in result]
        if slice_three is not None:
            for i in range(len(result)):
                result[i] = [line[slice_three] for line in result[i]]
        if slice_four is not None:
            for i in range(len(result)):
                for j in range(len(result[i])):
                    result[i][j] = [line[slice_four] for line in result[i][j]]
        return Matrix(result)

    slice = __slice__

    def __getitem__(self, key):
        return self._matrix[key]

    def __transposed__(self):
        result = list()
        for i in range(self._sizes[1]):
            result.append(list())
        for i in range(self._sizes[0]):
            for j in range(self._sizes[1]):
                result[j].append(self._matrix[i][j])
        return Matrix(result)

    transposed = property(__transposed__)

    def __add__(self, other):
        try:
            if isinstance(other, Matrix):
                return self.__matrix_addition__(other)
            elif isinstance(other, (int, float)):
                return self.__number_addition__(other)
            else:
                raise AdditionValueError
        except AdditionValueError:
            print(AdditionValueError._error)

    def __matrix_addition__(self, other):
        try:
            if self._sizes != other._sizes:
                raise AdditionSizeError
            result = list()
            for i in range(self._sizes[0]):
                if self._sizes[1] != 0:
                    result.append(list())
                    for j in range(self._sizes[1]):
                        if self._sizes[2] != 0:
                            result[i].append(list())
                            for k in range(self._sizes[2]):
                                if self._sizes[3] != 0:
                                    result[i][j].append(list())
                                    for m in range(self._sizes[3]):
                                        result[i][j][k].append(0)
                                        result[i][j][k][m] = self._matrix[i][j][k][m] + other._matrix[i][j][k][m]
                                else:
                                    result[i][j].append(0)
                                    result[i][j][k] = self._matrix[i][j][k] + other._matrix[i][j][k]
                        else:
                            result[i].append(0)
                            result[i][j] = self._matrix[i][j] + other._matrix[i][j]
                else:
                    result.append(0)
                    result[i] = self._matrix[i] + other._matrix[i]
            return Matrix(result)
        except AdditionSizeError:
            print(AdditionSizeError._error)
            return None

    def __number_addition__(self, number):
        result = list()
        for i in range(self._sizes[0]):
            if self._sizes[1] != 0:
                result.append(list())
                for j in range(self._sizes[1]):
                    if self._sizes[2] != 0:
                        result[i].append(list())
                        for k in range(self._sizes[2]):
                            if self._sizes[3] != 0:
                                result[i][j].append(list())
                                for m in range(self._sizes[3]):
                                    result[i][j][k].append(0)
                                    result[i][j][k][m] = self._matrix[i][j][k][m] + number
                            else:
                                result[i][j].append(0)
                                result[i][j][k] = self._matrix[i][j][k] + number
                    else:
                        result[i].append(0)
                        result[i][j] = self._matrix[i][j] + number
            else:
                result.append(0)
                result[i] = self._matrix[i] + number
        return Matrix(result)

    def __mul__(self, other):
        try:
            if isinstance(other, Matrix):
                return self.__matrix_multiplication__(other)
            elif isinstance(other, (int, float)):
                return self.__number_multiplication__(other)
            else:
                raise MultiplicationValueError
        except MultiplicationValueError:
            print(MultiplicationValueError._error)

    def __matrix_multiplication__(self, other):
        try:
            if self._sizes[1] != other._sizes[0]:
                raise MultiplicationSizeError
            other_transposed = other.transposed
            result = list()
            for i in range(self._sizes[0]):
                result.append(list())
                for j in range(other_transposed._sizes[0]):
                    result[i].append(0)
                    for k in range(self._sizes[1]):
                        result[i][j] += self._matrix[i][k] * other.transposed._matrix[j][k]
            return Matrix(result)
        except MultiplicationSizeError:
            print(MultiplicationSizeError._error)

    def __number_multiplication__(self, number):
        result = list()
        for i in range(self._sizes[0]):
            if self._sizes[1] != 0:
                result.append(list())
                for j in range(self._sizes[1]):
                    if self._sizes[2] != 0:
                        result[i].append(list())
                        for k in range(self._sizes[2]):
                            if self._sizes[3] != 0:
                                result[i][j].append(list())
                                for m in range(self._sizes[3]):
                                    result[i][j][k].append(0)
                                    result[i][j][k][m] = self._matrix[i][j][k][m] * number
                            else:
                                result[i][j].append(0)
                                result[i][j][k] = self._matrix[i][j][k] * number
                    else:
                        result[i].append(0)
                        result[i][j] = self._matrix[i][j] * number
            else:
                result.append(0)
                result[i] = self._matrix[i] * number
        return Matrix(result)

