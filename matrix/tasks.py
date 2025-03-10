def get_max(A):
    """
        Return the index of the max element in matrix
    """
    max_el = A[0][0]
    max_row_ix, max_col_ix = 0, 0
    for row in range(len(A)):
        for col in range(len(A[row])):
            if A[row][col] > max_el:
                max_el = A[row][col]
                max_row_ix = row
                max_col_ix = col
    return max_row_ix, max_col_ix


def star_array(size):
    """
        Return array with a star pattern
    """
    mid_diag_idx = size // 2
    dest_array = [[None for j in range(size)] for i in range(size)]
    for row in range(len(dest_array)):
        for col in range(len(dest_array[row])):
            if row == col or row == mid_diag_idx or col == mid_diag_idx or col == size - row -1:
                dest_array[row][col] = "*"
            else:
                dest_array[row][col] = '.'
    return dest_array

def chess_desc(row, col):
    """
        Return array with a chess desk pattern
    """
    dest_array = [[None for j in range(col)] for i in range(row)]
    for row in range(len(dest_array)):
        for col in range(len(dest_array[row])):
            if (row + col) % 2 == 1:
                dest_array[row][col] = "*"
            else:
                dest_array[row][col] = '.'
    return dest_array


def additional_diagonal(size):
    dest_array = [[None for j in range(size)] for i in range(size)]
    # Additional diag elements [i][N -i -1]
    for row in range(len(dest_array)):
        for col in range(len(dest_array[row])):
            if col < size - row - 1:
                dest_array[row][col] = 0
            elif col == size - row - 1:
                dest_array[row][col] = 1
            else:
                dest_array[row][col] = 2
    return dest_array




def swap_columns (A, i, j):
    for row in range(len(A)):
        A[row][i], A[row][j] = A[row][j], A[row][i]
    return A
    

def is_symmetrical(A):
    for row in range(len(A)):
        for col in range(len(A[row])):
            if A[row][col] != A[col][row]:
                return False
    return True

def matrix_transponantion(n, m, A):
    result_matrix = [[0 for j in range(n)] for i in range(m)]
    print(result_matrix)
    for row in range(len(A)):
        for col in range(len(A[row])):
            result_matrix[col][row] = A[row][col]
    return result_matrix


def swap_diagonals(A, N):
    for row in range(len(A)):
        for col in range(len(A[row])):
            if row == col:
                A[row][col], A[N - row - 1][row] = A[N - row -1][row], A[row][col]