def palindromo_maximo(P):
    n = len(P)
    if n <= 1:
        return P

    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    inicio = 0
    tamanho_maximo = 1

    for i in range(n - 1):
        if P[i] == P[i + 1]:
            dp[i][i + 1] = True
            inicio = i
            tamanho_maximo = 2

    for tamanho in range(3, n + 1):
        for i in range(n - tamanho + 1):
            j = i + tamanho - 1
            if P[i] == P[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if tamanho > tamanho_maximo:
                    inicio = i
                    tamanho_maximo = tamanho
    return P[inicio:inicio + tamanho_maximo]

# Exemplo
sequencia = "ACGTGTCAAAATCG"
resultado = palindromo_maximo(sequencia)
print("\nSubsequência palíndroma de tamanho máximo:\n", resultado)