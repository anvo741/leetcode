# https://leetcode.com/problems/group-anagrams/
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
# given a string, helper function that returns sorted list of letters ascending

def get_letters(str):
  letters = [i for i in str]
  letters.sort()
  return ''.join(letters)


def group_anagrams(lst):
  anagrams = {}
  for i in lst:
    if get_letters(i) in anagrams:
      anagrams[get_letters(i)].append(i)
    else:
      anagrams[get_letters(i)] = [i]
  return [anagrams[i] for i in anagrams]