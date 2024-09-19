import matrix as mx
import numpy as np

M = [[1, 1, 2],
     [3, 0, 1],
     [0, 3, 3]]

Mnp = np.array([[1, 1, 2],
                [3, 0, 1],
                [0, 3, 3]])

#1)
print("printing")
mx.print_matrix(M)
print(Mnp)

#2), 3)
print("\nheight, width")
print(mx.matrix_height(M), mx.matrix_width(M))
print(np.shape(M))

#4)
print("\ncreating a matrix")
N = mx.create_matrix(2, 3)
mx.print_matrix(N)

#5)
print("\nis_square")
print(mx.is_square(M))

#6)
print("\nsubmatrix")
mx.print_matrix(mx.submatrix(M, 1, 1))

#7)
print("\nmatrix_times_number")
mx.print_matrix(mx.matrix_times_number(3, M))
print(3*Mnp)

#8)
print("\nmatrix_addition")
N = [[0, 1, 1],
     [1, 9, 8],
     [7, 1, 1]]
Nnp = np.array([[0, 1, 1],
                [1, 9, 8],
                [7, 1, 1]])

mx.print_matrix(mx.matrix_addition(M, N))
print(Mnp+Nnp)

#9)
print("\nmatrix_subtraction")
mx.print_matrix(mx.matrix_subtraction(M, N))
print(Mnp-Nnp)

#10)
print("\nmatrix_multiplication")
mx.print_matrix(mx.matrix_multiplication(M, N))
print(np.matmul(Mnp, Nnp))

#11)
print("\nidentity")
mx.print_matrix(mx.identity(4))

#12)
print("\nzero_marix")
mx.print_matrix(mx.zero_matrix(2, 4))

#13)
print("\nrandom_matrix")
mx.print_matrix(mx.random_matrix(3, 2))

#14)
print("\ntranspose")
mx.print_matrix(mx.transpose(M))

#15)
print("\nis_symetric")
O = [[1, 0],
     [0, 2]]

print(mx.is_symetric(M))
print(mx.is_symetric(O))

#16)
print("\nhermit")
P = [[2, -1j],
     [1j, 3]]

mx.print_matrix(mx.hermit_transpose(P))

#17)
print("\nis_hermitian")
Q = [[2+1j, 3+1j],
     [3+1j, 0]]
print(mx.is_hermitian(P))
print(mx.is_hermitian(Q))

#18)
print("\nrow_echelon")
mx.print_matrix(mx.row_echelon(M))

#19)
print("\nrank")
R = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]

print(mx.rank(M))
print(mx.rank(R))

#20, 21)
print("\ndeterminant")
print(mx.determinant(M))
print(mx.determinant_2(M))
print(np.linalg.det(Mnp))

#22)
print("\nis_regular")
print(mx.is_regular(M))
print(mx.is_regular(R))

#23)
print("\ninverse")
mx.print_matrix(mx.inverse(M))
print(np.linalg.inv(Mnp))

#24)
print("\npositive definite")
S = [[3, 1],
     [1, 2]]
Snp = np.array([[3, 1],
                [1, 2]])

print(mx.is_pos_def(M))
print((np.all(np.linalg.eigvals(Mnp)) > 0) and mx.is_hermitian(M))
print(mx.is_pos_def(S))
print((np.all(np.linalg.eigvals(Snp)) > 0) and mx.is_hermitian(S))

#25)
print("\npositive semidefinite")
print(mx.is_pos_semidef(M))
print((np.all(np.linalg.eigvals(Mnp)) >= 0) and mx.is_hermitian(M))

#26)
print("kvad_rce")
print(mx.kvad_rce(1, 2, 1))

#27)
print("\nis_real")
print(mx.is_real(M))
print(mx.is_real(Q))

#28)
print("\ncomplex conjugate")
print(mx.c_conj(1+3j))

#29)
print("\ncholesky")
mx.print_matrix(mx.cholesky(S))
print(np.linalg.cholesky(Snp))
