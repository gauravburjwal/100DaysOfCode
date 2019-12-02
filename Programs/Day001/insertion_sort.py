def insertion_sort(nums):
  for j in range(1, len(nums)):
    key = nums[j]
    i = j - 1
    while i >= 0 and nums[i] > key:
      nums[i + 1] = nums[i]
      i = i - 1
    nums[i + 1] = key
  return nums



nums = [9,7,4,2,8]
print(nums)
nums = insertion_sort(nums)
print(nums)