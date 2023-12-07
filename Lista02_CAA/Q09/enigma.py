class Item:
    def __init__(self, Chave):
        self.Chave = Chave

def Enigma2(A, i, j):
    x = A[(i + j) // 2].Chave
    while True:
        while A[i].Chave < x:
            i += 1
        while A[j].Chave > x:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        if i > j:
            break

def Enigma1(A, m, n):
    i, j = m, n
    Enigma2(A, i, j)
    if m < j:
        Enigma1(A, m, j)
    if i < n:
        Enigma1(A, i, n)

# Exemplo
itens = [Item(3), Item(1), Item(4), Item(2)]
Enigma1(itens, 0, len(itens) - 1)
for item in itens:
    print(item.Chave, end=' ')


'''
A função enigma recursiva é uma implementação do algoritmo QuickSort, que tem um custo médio de O(n log n) e um custo 
no pior caso de O(n^2). A função Enigma1 chama a função Enigma2 uma vez e depois chama a si mesma recursivamente duas 
vezes. Portanto, o custo total da função Enigma1 depende do custo da função Enigma2.  No melhor caso, o vetor já está 
ordenado e o custo de Enigma2 é O(n log n). No pior caso, o vetor está ordenado em ordem inversa e o custo de Enigma2 
é O(n^2). Portanto, o custo total da função Enigma1 é O(n^2) no pior caso e O(n log n) no caso médio.
A complexidade de tempo da função Enigma1 é O(n log n), pois o algoritmo realiza uma operação n log n no pior caso, 
o que a torna um algoritmo que pode ser eficiente ou ineficiente, dependendo da forma como a Enigma2 é implementada.
'''