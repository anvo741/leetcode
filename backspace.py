''' 
Given two strings S and T, return if they are equal when both are typed
into empty text editors. # means a backspace characer.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: s = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1. 1 <= S.length <= 200
2. 1 <= T.length <= 200
3. S and T only contain lowercase letters and '#' characters.
'''

# resolve what S will be
# resolve what T will be
# compare the two

# helper function to resolve string
def resolve_text(string):
  text = ''
  for char in string:
    if char != "#":
      text = text + char
    else:
      text = text[:-1]
  return text

def is_text_same(S, T):
  s_text = resolve_text(S)
  t_text = resolve_text(T)
  return s_text == t_text


# example 1 True
print(is_text_same("ab#c", "ad#c"))

# example 2 True
print(is_text_same("ab##", "c#d#"))

# Example 3 True
print(is_text_same("a##c","#a#c"))

# Example 4 False
print(is_text_same("a#c", "b"))

# True
print(is_text_same('',''))
#True
print(is_text_same('###', '##'))
#True
print(is_text_same('cat', 'cat'))
#False
print(is_text_same('', ' '))
