# stock gains
# building tic tac toe / connect 4

# https://leetcode.com/problems/ugly-number/
# a number is prime if it is only divisible by itself and 1.

# ex: 4
# check if n is divisible by any ugly_factors. if it's not divisible
# by any of them, return False
# 

def is_ugly(num):
	if num < 1:
		return False
	for factor in [2,3,5]:
		while num % factor == 0:
			num = num / factor
	return num == 1