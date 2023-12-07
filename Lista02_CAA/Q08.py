# primeiro
'''
O primeiro algoritmo é uma implementação Bubble Sort com dois loops. O loop externo é executado n vezes e o interno é executado n vezes 
para cada iteração do loop externo. O algoritmo compara todos os pares de elementos do vetor e trocar os elementos de posição se necessário.

Pior caso:
Ocorre quando a matriz está na ordem inversa. Nesse caso, o algoritmo executará n-1 iterações externas, cada uma com n-1 iterações internas. 
Portanto, a complexidade no pior caso é O(n^2).

Melhor caso:
Ocorre quando a matriz já está ordenada. Nesse caso, o algoritmo não realizará nenhuma troca. 
Portanto, a complexidade no melhor caso é O(n).

Caso médio:
Ocorre quando a matriz está em alguma ordem aleatória. Nesse caso, a complexidade é O(n^2).
'''

# segundo
'''
O segundo algoritmo é uma variação do Bubble Sort que usa uma variável booleana troca para verificar se houve trocas no loop interno. 
O loop externo é executado até que não haja mais trocas no loop interno e interno é executado n vezes para cada iteração do loop externo.

Pior caso:
Ocorre da mesma forma que o pior caso da função bubble sort. Portanto, a complexidade no pior caso é O(n^2).

Melhor caso:
Também ocorre da mesma forma que o melhor caso da função bubble sort. Portanto, a complexidade no melhor caso é O(n).

Caso médio:
Igual o caso médio da função bubble sort. Portanto, a complexidade é O(n^2).
'''

# terceiro
'''
O terceiro algoritmo tem três loops. O loop externo é executado n-1 vezes, o loop intermediário n-i vezes para cada 
iteração do loop externo e o interno é executado j vezes para cada iteração do loop intermediário. 

AlgumaCoisa:
A função AlgumaCoisa percorre a matriz A em um loop externo de 1 a n, um loop interno de i+1 a n+1 e um loop interno de 1 a j+1. 
Portanto, a complexidade da função é O(n^2).

FAlgumaCoisa2:
A função AlgumaCoisa2 percorre a matriz A em um loop externo de 1 a n+1, um loop interno de i+1 a n e um loop interno de 1 a j+1. 
Portanto, a complexidade da função é O(n^2).
'''