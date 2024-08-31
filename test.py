import matrix as mx

M = [[2, 1, 1, 1],
     [1, 2, 1, 1],
     [1, 1, 3, 1],
     [1, 1, 1, 2]]

N = [[4, 1, 2],
     [1, 2, 1],
     [2, 1, 4]]

O = [[2, 1],
     [1, 1]]


mx.print_matrix(mx.cholesky(M))
print(mx.c_conj(3+2j))
