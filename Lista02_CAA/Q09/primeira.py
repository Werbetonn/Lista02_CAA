def pesquisa1(A, n):
  if n == 1:
    if A[0] == x:
      return True
    else:
      return False
  else:
 
    m = n // 3
    A1 = A[:m]
    A2 = A[m:2 * m]
    A3 = A[2 * m:]

    return (pesquisa1(A1, m) or
            pesquisa1(A2, m) or
            pesquisa1(A3, m))
  

'''
Essa função recursiva tem um custo de O(n^3) no pior caso, pois é chamada recursivamente n/3 vezes, 
e cada chamada tem um custo de n^3. No melhor caso, a função não é chamada recursivamente, e seu custo é O(1).
A complexidade de tempo da função Pesquisa1 é O(n^3), pois o algoritmo realiza uma operação n^3 no pior caso, 
o que a torna um algoritmo ineficiente
'''