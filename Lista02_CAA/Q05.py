#Algoritmo 1
'''
O primeiro algoritmo tem dois loops aninhados. O loop externo é executado n vezes, já interno é executado n vezes para cada 
iteração do loop externo. O laço é n*n=n^2, o custo do primeiro laço é de O(n) executado n vezes. O custo do segundo laço é
de O(n), também executado n vezes, portanto, a complexidade de tempo desse algoritmo é quadrática e o custo total do loop é O(n^2).
'''

#Algoritmo 2
'''
O segundo algoritmo tem um loop externo que é executado log2(n) vezes e um loop interno que é executado n vezes para cada 
iteração do loop externo, ele incrementa i multiplicando por 2 a cada iteração e executa aproximadamente log2(n) vezes  até 
ultrapassar n, o custo total do loop é O(n log n), do laço externo é log2(n) e do interno é n. O primeiro laço é O(n), pois é 
executado n vezes, do segundo laço é de O(n), também executado n vezes. No entanto, o laço interno é executado apenas para 
valores de i <= n/2. Portanto, o custo total do algoritmo é de O(n/2 * n) = O(n^2/2).
'''

#Algoritmo 3
'''
O terceiro algoritmo tem um loop externo que é executado log2(n) vezes e um loop interno que é executado n/i vezes para cada 
iteração do loop externo. O laço externo também incrementa i multiplicando por 2 a cada iteração, já o interno incrementa j por i.
O número de vezes que o laço externo é executado é log2(n), já o número de iterações do laço interno varia de acordo com i, que é 
multiplicado por 2 a cada iteração. O custo desse algoritmo está entre O(n log n) e O(n), mais próximo de O(n log n) para a maioria 
dos casos de entrada comuns. O custo do primeiro laço é de O(n), executado n vezes. O custo do segundo é de O(n log n), pois o laço 
é executado log n vezes, e cada iteração do laço interno custa O(n). Portanto, o custo total do loop é O(n log n).
'''