# Multi-Dimensional Array (Matrix) Implementation

class Matrix:
    def __init__(self, rows, cols):
        # Initialize a matrix with the given number of rows and columns
        self.rows = rows
        self.cols = cols
        self.matrix = [[None for _ in range(cols)] for _ in range(rows)]
    
    def insert(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            raise IndexError("Invalid row or column index")
        self.matrix[row][col] = value

    def get_value(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise IndexError("Invalid row or column index")
        return self.matrix[row][col]

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def transpose(self):
        transposed = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return transposed

# Example Usage:
if __name__ == "__main__":
    mat = Matrix(3, 3)
    mat.insert(0, 0, 1)
    mat.insert(0, 1, 2)
    mat.insert(0, 2, 3)
    mat.insert(1, 0, 4)
    mat.insert(1, 1, 5)
    mat.insert(1, 2, 6)
    mat.insert(2, 0, 7)
    mat.insert(2, 1, 8)
    mat.insert(2, 2, 9)

    print("Original Matrix:")
    mat.print_matrix()
    
    print("\nTransposed Matrix:")
    transposed = mat.transpose()
    for row in transposed:
        print(row)
