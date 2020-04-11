# https://www.interviewcake.com/question/python3/reverse-words?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23288:%20Reverse%20Words&utm_medium=email&utm_medium=email
'''
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))
'''

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

# reverse message in place

def reverse_chars(lst, start, stop):
	while start < stop:
		temp = lst[start]
		lst[start] = lst[stop]
		lst[stop] = temp
		start += 1
		stop -= 1
	return lst


def reverse_words(lst):
	# reverse entire list first. this produces the correct word order.
	reverse_chars(lst, 0, len(lst) - 1)
	current_word_start = 0
	for i in range(len(lst) + 1):
		# signals end of a word
		if i == len(lst) or lst[i] == ' ':
			reverse_chars(lst, current_word_start, i - 1)
			current_word_start = i + 1
	return lst