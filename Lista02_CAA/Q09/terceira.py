def pesquisa3(A, n):
  if n == 1:
    if A[0] == x:
      return True
    else:
      return False
  else:

    A.sort()
    A1 = A[0:n // 2]
    A2 = A[n // 2:]

    return pesquisa3(A2, n // 2)
  
'''
Essa função recursiva tem um custo de O(n log n) no pior caso, pois a função é chamada recursivamente 3n/2 vezes, 
e cada chamada descarta 1/3 dos elementos. No melhor caso, a função não é chamada recursivamente, e seu custo é O(1).
A complexidade de tempo da função Pesquisa3 é O(n log n), pois o algoritmo realiza uma operação n log n no pior caso, 
o que a torna tão eficiente quanto a Pesquisa2.

'''