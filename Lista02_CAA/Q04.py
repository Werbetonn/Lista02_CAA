def elemento_majoritario(nums):
    count = 0
    candidato = None

    for num in nums:
        if count == 0:
            candidato = num
        count += 1 if num == candidato else -1

    return candidato

# Exemplo de uso
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
resultado = elemento_majoritario(nums)
print("Elemento majoritário:", resultado)