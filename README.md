Funkce jsou nasledující:

1) print_matrix(A)
vytiskne matici A jako tabulku

2) matrix_height(A)
vrátí výšku matice A

3) matrix_width(A)
vrátí šířku matice(A)

4) create_matrix(m, n)
umožní uživateli si na výstupu vytvořit matici typu mxn

5) is_square(A)
vrátí True když je matice čtvercova a False v opačném případě

6) submatrix(A, i, j)
vrátí podmatici vzniklou vynecháním i-tého řádku a j-tého sloupce z matice A

7) matrix_times_number(x, A)
vrátí matici A vynásobenou číslem x

8) matrix_addition(A, B)
vrátí součet matic A a B

9) matrix_subtraction(A, B)
vrátí rozdíl A-B

10) matrix_multiplication(A, B)
vrátí součin A*B

11) identity(n)
vrátí jednotkovou matici řádu n

12) zero_matrix(m, n)
vrátí matici typu mxn se samými nulami

13) random_matrix(m, n)
vrátí matici typu mxn s náhodými čísly

14) transpose(A)
vrátí matici transponovanou k A

15) is_symetric(A)
vrátí True když je matice symetrická, jinak False

16) hermit_transpose(A)
vrátí matici hermitovsky sdruženou k A

17) is_hermitian(A)
vrátí True pokud je matice hermitovská, jinak False

18) def row_echelon(A)
vrátí odstupňovaný tvar matice A

19) rank(A)
vrátí hodnost matice A

20) determinant(A)
vrátí determinant matice A
matici převede na odstupňovaný tvar ekvivalentními úpravami, pak spočítá součin na hlavní diagonále

21) determinant_2(A)
spočítá determinant pomocí rozvoje podle prvního řádku

22) is_regular(A)
vrátí True pokud je A regulární, jinak False

23) inverse(A)
vrátí inverzní matici k matici A

24) is_pos_def(A)
vrátí True pokud je A pozitivně definitní, jinak False

25) is_pos_semidef(A)
vrátí True pokud je A pozitivně semidefinitní, jinak False

26) kvad_rce(a, b, c)
vrátí kořeny kvadratické rovnice typu a*x^2 + b*x + c = 0

27) is_real(A)
vrátí True pokud jsou všechna čísla v A reálná, jinak false

28) c_conj(z)
vrátí číslo komplexně sdružené k z

29) cholesky(A)
vrátí choleského rozklad matice A
