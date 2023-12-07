#Solução Melhor Caso
def melhor_caso(nums, X):
  seen = set()

  for i in range(len(nums)):
    if X - nums[i] in seen:
      return [i, nums.index(X - nums[i])]
    seen.add(nums[i])

  return None