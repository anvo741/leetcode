# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/

def singleNumber(nums):
	# sort nums in place
	nums.sort()
	# iterate through nums
	# if a num is not followed by itself, then return the num
	i = 0
	while i < len(nums):
	    if i == len(nums) - 1:
	        return nums[i]
	    elif i % 2 == 0 and nums[i] != nums[i+1]:
	        return nums[i]
	    else:
	        i +=1