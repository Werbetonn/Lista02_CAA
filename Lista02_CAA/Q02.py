def multiplicar_matriz(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    C = [[0 for _ in range(n)] for _ in range(n)]

    sub_matriz = n // 3
    for i in range(3):
        for j in range(3):
            A_sub = [row[j * sub_matriz:(j + 1) * sub_matriz] for row in A[i * sub_matriz:(i + 1) * sub_matriz]]
            B_sub = [row[j * sub_matriz:(j + 1) * sub_matriz] for row in B[i * sub_matriz:(i + 1) * sub_matriz]]
            C_sub = multiplicar_matriz(A_sub, B_sub)

            for k in range(sub_matriz):
                for l in range(sub_matriz):
                    C[i * sub_matriz + k][j * sub_matriz + l] = C_sub[k][l]
    return C

#Exemplo
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

resultado = multiplicar_matriz(A, B)
for row in resultado:
    print(row)