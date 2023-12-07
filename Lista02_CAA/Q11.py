def mesclagem_matrizes(nums1, m, nums2, n):
 
  p1 = 0
  p2 = 0
  while p1 < m and p2 < n:
    if nums1[p1] <= nums2[p2]:
      nums1[p1 + n] = nums1[p1]
      p1 += 1
    else:
      nums1[p1 + n] = nums2[p2]
      p2 += 1

  if p1 == m:
    for i in range(p2, n):
      nums1[i + n] = nums2[i]

#exemplo
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

mesclagem_matrizes(nums1, m, nums2, n)
print(nums1)
# Saída: [1,2,2,3,5,6]