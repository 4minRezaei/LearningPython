class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string

    def row(self, index):
        row = (self.matrix.split('\n')[index -1]).split()
        for i in range(len(row)):
            row[i] = int(row[i])
        return row
        
    def column(self, index):
        column = []
        for row in (self.matrix.split('\n')):
            column.append(int(row.split()[index-1]))
        return column
