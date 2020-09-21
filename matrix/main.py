from base import print_arr
from tasks import additional_diagonal

size = int(input().split()[0])

A = additional_diagonal(size)
print_arr(A)