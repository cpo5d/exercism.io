class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        # for each element in a list of the matrix elements split by \n, create a row in the matrix
        for r in matrix_string.splitlines():
            # assemble each row in the matrix by iterating through the values in the split row string
            self.matrix.append([int(c) for c in r.split()])

    def row(self, index):
        # try to return the called for row if it exists
        try:
            return self.matrix[index - 1]
        # if the index given is not valid, return None
        except IndexError:
            return None

    def column(self, index):
        try:
            # return a list of the correct column index in each row
            return [row[index-1] for row in self.matrix]
        # if the index given is not valid, return None
        except IndexError:
            return None