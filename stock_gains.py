'''
You will be given a list of stock prices for a given day and your goal is to 
return the maximum profit that could have been made by buying a stock at the 
given price and then selling the stock later on. For example if the input is: 
max_b = 1
max_s = 4

then your program should return 16 because if you bought the stock at $24 and 
sold it at $40, a profit of $16 was made and this is the largest profit that 
could be made. If no profit could have been made, return -1.

https://coderbyte.com/algorithm/stock-maximum-profit
'''

# iterate through list.
# keep track of the running best gain.
def max_stock_gains(lst):
	current_best = -1
	baseline = 0
	current = 1
	while baseline < len(lst) - 1:
		while current < len(lst):
			diff = lst[current] - lst[baseline]
			if diff > current_best:
				current_best = diff
			current += 1
		baseline += 1
		current = baseline + 1
	return current_best


#[45, 24, 22, 31, 40, 21, 50] 
#                     b
#                          s  
def max_stock_gains_better(lst):
	current_best = -1 # 9 18
	buy = 0
	sell = 1
	lowest_buy = buy
	max_sell = sell
	
	while buy < sell and sell < len(lst):
		profit = lst[sell] - lst[buy]
		if profit > current_best:
			current_best = profit
			max_sell = sell
			lowest_buy = buy
		if profit < 0:
			buy = sell
			lowest_buy = sell
		sell += 1 
	return current_best
	