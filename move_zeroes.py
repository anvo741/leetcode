# https://leetcode.com/problems/move-zeroes/submissions/

def moveZeroes(nums):
	"""
	Do not return anything, modify nums in-place instead.
	"""
	current = 0
	non_zero = 0
	temp = 0
	if 0 in nums:
		while current < len(nums):
			if nums[current] != 0:
				temp = nums[non_zero]
				nums[non_zero] = nums[current]
				nums[current] = temp
				non_zero += 1
			current += 1
	return nums