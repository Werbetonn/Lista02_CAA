def buscar_posicao(nums, alvo):

  n = len(nums)
  if n == 0:
    return -1

  inicio = 0
  fim = n - 1
  while inicio <= fim:
    meio = (inicio + fim) // 2
    if nums[meio] == alvo:
      return meio
    elif nums[meio] < alvo:
      inicio = meio + 1
    else:
      fim = meio - 1

  return -1

#exemplo
nums = [1, 3, 5, 6]
alvo = 5

print(buscar_posicao(nums, alvo))
#saída: 2