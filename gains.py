def find_max_diff(lst):
	if len(lst):
		max_diffs = []
		for i in range(len(lst)-1):
			diffs = []
			i = 0
			while i < len(lst)-1:
				diff = lst[i] - lst[i+1]
				diffs.append(diff)
				i += 1
			max_diff = max(diffs)
			max_diffs.append(max_diff)
		return max(max_diffs)