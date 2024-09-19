import cmath as cm
import math as m
import random as r

def print_matrix(A):
    #prehlednejsi zbusob pro zobrazeni matic
    if A == False:
        print("()")
    else:
        if type(A) == list:
            print("[ ", end = '')
            print(A[0], ",")
            for i in A[1:-1]:
                print(" ",  i, ",")
            print(" ", A[-1], "]")

def matrix_height(A):
    if A == False:
        return 0
    else:
        return len(A)

def matrix_width(A):
    if  A == False:
        return 0
    else:
        return len(A[0])

def create_matrix(m, n):
    #vytvori ze vstupu matici typu mxn
    A = [[float(input()) for j in range(n)] for i in range(m)]
    return A

def is_square(A):
    if matrix_height(A) == matrix_width(A):
        return True
    else:
        return False

def submatrix(A, i, j):
    #vrati podmatici vzniklou vynechanim i-teho radku a j-teho sloupce
    m = matrix_height(A)
    n = matrix_width(A)
    #zde si vytvarime kopii matice, jinak by fce zmenila puvodni matici misto vraceni nove
    B = [[0 for o in range(n)] for p in range(m)]
    for x in range(m):
        for l in range(n):
            B[x][l] = A[x][l]
    B.pop(i)
    for k in range(n - 1):
        B[k].pop(j)
    return B

def matrix_times_number(x, A):
    C = [[x*A[i][j] for j in range(matrix_width(A))] for i in range(matrix_height(A))]
    return C

def matrix_addition(A, B):
    if matrix_height(A) != matrix_height(B) or matrix_width(A) != matrix_width(B):
        return False
    else:
        C = [[A[i][j] + B[i][j] for j in range(matrix_width(A))] for i in range(matrix_height(A))]
        return C

def matrix_subtraction(A, B):
    #POZOR! neni komutativni
    return matrix_addition(A, matrix_times_number(-1, B))

def matrix_multiplication(A, B):
    #taky ne komutativni
    if matrix_width(A) != matrix_height(B):
        return False
    else:
        m = matrix_height(A)
        n = matrix_width(A)
        p = matrix_width(B)
        C = [[0 for j in range(p)] for i in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    C[i][j] = C[i][j] + A[i][k]*B[k][j]
        return C

def identity(n):
    #vrati jednotkovou matici typu nxn:
    I = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

def zero_matrix(m, n):
    #vrati matici typu mxn se samymi nulami
    O = [[0 for j in range(n)] for i in range(m)]
    return O

def random_matrix(m, n):
    #vrati matici s nahodnymi celymi cisly
    #matice je typu mxn
    #hodnoty jsou mezi minus jeden milion a jeden milion
    R = [[r.randint(-1000000, 1000000) for j in range(n)] for i in range(m)]
    return R

def transpose(A):
    m = matrix_height(A)
    n = matrix_width(A)
    B = [[A[j][i] for j in range(m)] for i in range(n)]
    return B

def is_symetric(A):
    if is_square(A) == False:
        return False
    else:
        B = matrix_subtraction(A, transpose(A))
        maximum = abs(B[0][0])
        n = matrix_height(B)
        for i in range(n):
            for j in range(n):
                if abs(B[i][j]) > maximum:
                    maximum = abs(B[i][j])
        if maximum < 0.0000000000000001:
            return True
        else:
            return False

def hermit_transpose(A):
    m = matrix_height(A)
    n = matrix_width(A)
    B = [[(A[j][i].real - A[j][i].imag*1j) for j in range(m)] for i in range(n)]
    return B

def is_hermitian(A):
    if is_square(A) == False:
        return False
    else:
        if A == hermit_transpose(A):
            return True
        else:
            return False

def row_echelon(A):
    #funkce, ktera ekvivalentnimi upravami prevede matici na odstupnovany tvar
    m = matrix_height(A)
    n = matrix_width(A)
    r = min(m, n)
    B = [[0 for o in range(n)] for p in range(m)]
    for x in range(m):
        for l in range(n):
            B[x][l] = A[x][l]
    for i in range(r-1):
        if B[i][i] == 0:
            a = 0
            #zjisti, zda je v tomto sloupci vubec nejaky nenulovy prvek
            for j in range(i+1, m):
                if B[j][i] != 0:
                    #vymena radku
                    B[i], B[j] = B[j], B[i]
                    a += 1
                    break
            if a == 0:
                pass
            else:
                for j in range(i + 1, m):
                    if B[j][i] == 0:
                        pass
                    else:
                        for k in range(i, n):
                            #nasobeni radku a pricitani nasobku jineho
                            B[j][k] = (B[i][i] * B[j][k]) - (B[j][i] * B[i][k])
        else:
            for j in range(i+1, m):
                if B[j][i] == 0:
                    pass
                else:
                    hodnota = B[j][i]
                    for k in range(i, n):
                        # nasobeni radku a pricitani nasobku jineho
                        B[j][k] = (B[i][i] * B[j][k]) - (hodnota * B[i][k])
    #usporada radky taky, aby vsechny nulove byly dole
    for i in range(m):
        a = 0
        for j in range(n):
            if B[i][j] != 0:
                a += 1
                break
        if a == 0:
            for k in range(i, m-1):
                B[k], B[k+1] = B[k+1], B[k]
    return B


def rank(A):
    B = row_echelon(A)
    m = matrix_height(B)
    n = matrix_width(B)
    rank = m
    #projizdime matici zespoda dokud nenajdeme nenulovy radek
    for i in range(m-1, -1, -1):
        a = 0
        for j in range(n):
            if B[i][j] == 0:
                a += 1
        if a == n:
            rank -= 1
        else:
            break
    return rank

def determinant(A):
    #vypocet determinantu pomoci upravy na dolni trojuhelnikovy tvar
    if is_square(A) == False:
        return False
    else:
        n = matrix_height(A)
        det = 1
        B = [[0 for o in range(n)] for p in range(n)]
        for x in range(n):
            for l in range(n):
                B[x][l] = A[x][l]
        for i in range(n - 1):
            if B[i][i] == 0:
                a = 0
                for j in range(i + 1, n):
                    if B[j][i] != 0:
                        B[i], B[j] = B[j], B[i]
                        det = -det
                        a += 1
                        break
                if a == 0:
                    pass
                else:
                    for j in range(i + 1, n):
                        if B[j][i] == 0:
                            pass
                        else:
                            for k in range(i, n):
                                B[j][k] = (B[i][i] * B[j][k]) - (B[j][i] * B[i][k])
                                det = det*(1/B[i][i])
            else:
                for j in range(i + 1, n):
                    if B[j][i] == 0:
                        pass
                    else:
                        hodnota = B[j][i]
                        for k in range(i, n):
                            B[j][k] = (B[i][i] * B[j][k]) - (hodnota * B[i][k])
                        det = det*(1/B[i][i])
        for h in range(n):
            det = det*B[h][h]
        return det


def determinant_2(A, det = 0):
    #vypocet determinanatu pomoci rozvoje podle prvniho radku (pro zajimavost)
    if is_square(A) == False:
        return False
    else:
        n = matrix_height(A)
        if n == 1:
            return A[0][0]
        else:
            n = matrix_width(A)
            for i in range(n):
                det += (A[0][i])*((-1)**i)*determinant_2(submatrix(A, 0, i))
            return det

def is_regular(A):
    if is_square(A) == False:
        return False
    else:
        if abs(determinant_2(A)) < 0.0000000000000001:
            return False
        else:
            return True

def inverse(A):
    #vrati inverzni matici k matici A pomoci metody adjugovane matice
    det = determinant_2(A)
    if det == 0:
        return False
    else:
        n = matrix_height(A)
        B = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                B[i][j] = ((-1)**(i+j))*determinant_2(submatrix(A, j, i))
        B = matrix_times_number(1/det, B)
        return B

def is_pos_def(A):
    #funkce, ktera urci zda je matice pozitivne definitni metodou subdeterminantu
    if is_square(A) == False:
        return False
    else:
        n = matrix_width(A)
        B = [[0 for o in range(n)] for p in  range(n)]
        for x in range(n):
            for l in range(n):
                B[x][l] = A[x][l]
        a = 0
        for i in range(n):
            det = determinant_2(B)
            if det <= 0:
                a += 1
                break
            B = submatrix(B, 0, 0)
        if a == 0:
            return True
        else:
            return False

def is_pos_semidef(A):
    if is_square(A) == False:
        return False
    else:
        n = matrix_width(A)
        B = [[0 for o in range(n)] for p in  range(n)]
        for x in range(n):
            for l in range(n):
                B[x][l] = A[x][l]
        a = 0
        for i in range(n):
            det = determinant_2(B)
            if det < 0:
                a += 1
                break
            B = submatrix(B, 0, 0)
        if a == 0:
            return True
        else:
            return False

def kvad_rce(a, b, c):
    #vrati koreny kvadraticke rovnice tvaru ax^2 + bx + c = 0
    #spravne by melo byt a nenulove, ale tato funkce to vyresi i tak
    #muzou byt i komplexni koreny, nebo koeficienty
    if a == 0:
        if b == 0:
            if c == 0:
                return "vsechna koplexni cisla"
            else:
                return False
        else:
            #vysledky budeme vracet ve forme listu, aby se nam jednotlive slozky jednoduse zpristupnovaly
            return [-c/b, -c/b]
    else:
        if b**2-4*a*c == 0:
            return [-b/(2*a), -b/(2*a)]
        else:
            #abychom meli co nejcistsi vystupy, nebudeme u realnych cisel vypisovat imaginarni cast
            z1, z2 = (-b + cm.sqrt(b**2 - 4*a*c))/(2*a), (-b - cm.sqrt(b**2 - 4*a*c))/(2*a)
            if z1.imag == 0 and z2.imag == 0:
                return [z1.real, z2.real]
            elif z1.imag == 0 and z2.imag != 0:
                return [z1.real, z2]
            elif z1.imag != 0 and z2.imag == 0:
                return [z1, z2.real]
            else:
                return [z1, z2]

#def eigenvalues_2(A):
    #vrati vlastni cisla pro matice typu 2x2
    #ve finalni verzi mozna pribudne i pro matice typu 3x3
 #
  #  if matrix_height(A) != 2 or matrix_width(A) != 2:
   #     return False
    #else:
     #   a1 = 1
      #  a2 = -A[0][0] - A[1][1]
       # a3 = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        #return kvad_rce(a1, a2, a3)

#def eigenvectors(A):
    #vrati vlastni vektory pro matice typu 2x2
 #   B1 = matrix_subtraction(A, matrix_times_number(eigenvalues_2(A)[0], identity(2)))
  #  C1 = row_echelon(B1)
   # if C1[0][0] == 0:
    #    v1 = [1, 0]
    #elif C1[0][1] == 0:
     #   v1 = [0, 1]
    #else:
     #   v1 = [(-C1[0][1])/C1[0][0], 1]
    #B2 = matrix_subtraction(A, matrix_times_number(eigenvalues_2(A)[1], identity(2)))
    #C2 = row_echelon(B2)
    #if C2[0][0] == 0:
    #    v2 = [1, 0]
    #elif C2[0][1] == 0:
     #   v2 = [0, 1]
    #else:
     #   v2 = [(-C2[0][1]) / C2[0][0], 1]
    #return [v1, v2]

def is_real(A):
    m = matrix_height(A)
    n = matrix_width(A)
    a = 0
    for i in range(m):
        for j in range(n):
            if A[i][j].imag != 0:
                a += 1
                break
    if a == 0:
        return True
    else:
        return False

def c_conj(z):
    #vrati koplexne zdruzene cislo k cislu z
    if z.imag == 0:
        return z
    else:
        return z.real - z.imag*1j

def cholesky(A):
    #na vystupu vrati matici L z choleskeho rozkladu (A = L*L^T)
    #realne matice
    if is_real(A) == True:
        if is_pos_def(A) == False:
            return False
        else:
            n = matrix_height(A)
            L = [[0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(i+1):
                    if j == i:
                        x = 0
                        for k in range(i):
                            x += (L[i][k])**2
                        L[i][j] = round(m.sqrt(A[i][i] - x), 2)
                    else:
                        y = 0
                        for k in range(j):
                            y += L[i][k]*L[j][k]
                        L[i][j] = round((1/L[j][j])*(A[i][j]-y), 2)
            matice = [L, transpose(L)]
            return matice
    #komplexni matice
    else:
        if is_pos_semidef(A) == False:
            return False
        else:
            n = matrix_height(A)
            L = [[0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(i + 1):
                    if j == i:
                        x = 0
                        for k in range(i):
                            x += (L[i][k])*c_conj(L[i][k])
                        L[i][j] = round(m.sqrt(A[i][i] - x), 2)
                    else:
                        y = 0
                        for k in range(j):
                            y += L[i][k] * c_conj(L[j][k])
                        L[i][j] = round((1 / L[j][j]) * (A[i][j] - y), 2)
            matice = [L, transpose(L)]
            return matice






