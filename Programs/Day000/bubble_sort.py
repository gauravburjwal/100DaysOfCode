def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums

nums = [2,5,8,1,4,9]
print(nums)
nums = bubble_sort(nums)
print(nums)