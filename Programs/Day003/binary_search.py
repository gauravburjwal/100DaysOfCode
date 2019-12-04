def binary_search(nums, item):
	first = 0
	last = len(nums) - 1
	found = False
	while( first <= last and not found):
		mid = (first + last) // 2
		if nums[mid] == item :
			found = True
		else:
			if item < nums[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
