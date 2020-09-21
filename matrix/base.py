def print_arr(A):
  for row in range(len(A)):
    for col in range(len(A[row])):
      print(A[col][row], end = ' ')
    print()
