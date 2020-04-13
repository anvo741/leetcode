def is_happy(n):
  return is_happy_helper(n, set())

def is_happy_helper(n, sums):
  digits = str(n)
  running_sum = 0
  for digit in digits:
    running_sum = running_sum + int(digit) ** 2
  
  if running_sum == 1:
    return True
  
  if running_sum in sums:
  	return False
  else:
  	sums.add(running_sum)
  	return is_happy_helper(running_sum, sums)