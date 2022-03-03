class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        # split the provided matrix string so that it looks like ["1 2","3 4"]
        split_matrix_string = self.matrix_string.split("\n")
        self.matrix = []
        # for each element in the list above, create a row in the matrix
        for i in range(len(split_matrix_string)):
            row = []
            for j in range(len(split_matrix_string[i].split(" "))):
                # split the element in split_matrix_strix into individual items and convert to int before appending to row
                row.append(int(split_matrix_string[i].split(" ")[j]))
            self.matrix.append(row)

    def row(self, index):
        # check if the index given is valid
        if index <= len(self.matrix):
            return self.matrix[index - 1]
        # if the index given is not valid, return None
        else:
            return None

    def column(self, index):
        matrix_column = []
        i = 1
        # check if the index given is valid
        if index <= len(self.row(i)):
            # iterate through the rows of the matrix
            while self.row(i) is not None:
                # add the index-th item of the row to the column list after converting to int
                matrix_column.append(int(self.row(i)[index - 1]))
                i += 1
            return matrix_column
        # if the index given is not valid, return None
        else:
            return None