#Solução Simples
def solucao_simples(nums, X):

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == X:
        return [i, j]

  return None