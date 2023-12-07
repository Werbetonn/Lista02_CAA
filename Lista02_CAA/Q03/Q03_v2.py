#Solução Melhorada
def solucao_melhorada(nums, X):

  nums.sort()
  i = 0
  j = len(nums) - 1

  while i < j:
    if nums[i] + nums[j] == X:
      return [i, j]
    elif nums[i] + nums[j] < X:
      i += 1
    else:
      j -= 1

  return None