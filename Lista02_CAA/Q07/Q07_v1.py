def quadrados(nums):
    quadrados = [num ** 2 for num in nums]
    quadrados.sort()
    return quadrados

# Exemplo
nums = [-4, -1, 0, 3, 10]
resultado = quadrados(nums)
print("Quadrados em ordem não decrescente:", resultado)