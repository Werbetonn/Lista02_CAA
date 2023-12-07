#Solução O(n) usando outra abordagem (if e else)  mesclando dois arrays.

def quadrados(nums):
    n = len(nums)
    resultado = [0] * n
    left, right = 0, n - 1
    indice = n - 1

    while left <= right:
        quadrado_esquerda = nums[left] ** 2
        quadrado_direita = nums[right] ** 2

        if quadrado_esquerda > quadrado_direita:
            resultado[indice] = quadrado_esquerda
            left += 1
        else:
            resultado[indice] = quadrado_direita
            right -= 1
        indice -= 1
    return resultado

# Exemplo
nums = [-4, -1, 0, 3, 10]
resultado = quadrados(nums)
print("Quadrados em ordem não decrescente:", resultado)
