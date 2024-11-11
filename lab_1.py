import sys
import math
from contextlib import redirect_stdout 

def filter_words(words, letters):
	data = set (letters)
	result = [word for word in words if any(char in data for chat in word)]
	return result
