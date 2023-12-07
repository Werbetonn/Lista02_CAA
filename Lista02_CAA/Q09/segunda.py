def pesquisa2(A, n):
  if n == 1:
    if A[0] == x:
      return True
    else:
      return False
  else:

    m = A[0]
    for i in range(1, n):
      if A[i] > m:
        m = A[i]

    A1 = A[0:i]
    A2 = A[i:]

    return pesquisa2(A2, 3 * n // 5)
  
'''
Essa função recursiva tem um custo de O(n) no pior caso, pois a função é chamada recursivamente 3n/5 vezes, e cada 
chamada descarta 2/5 dos elementos. No melhor caso, a função não é chamada recursivamente, e seu custo é O(1).
A complexidade de tempo da função Pesquisa2 é O(n log n), pois o algoritmo realiza uma operação n log n no pior caso, 
o que a torna mais eficiente que a Pesquisa1.
'''