
'''
This simple program converts a number in base a into
a number in base b in which a and b are both between 2 and 16.
'''

def convert_to_base_10(x, base):
	result = 0
	if base < 2 or base > 36:
		print('Base should be between 2 and 36')
		return False, result
	mult = 1
	for ch in reversed(x.strip()):
		if ch < '0' or ch > 'Z' or (ch > '9' and ch < 'A'):
			return False, result
		j = ord(ch) - ord('0') if ch <= '9' else ord(ch) - ord('A') + 10
		if j >= base:
			return False, result
		result += mult * j
		if mult > 1.0e30 / base:
			return False, result
		mult *= base
	return True, result

def convert_from_base_10(x, base):
	result = ''
	if base < 2 or base > 36:
		print('Base should be between 2 and 36')
		return False, result
	while int(x) > 0:
		n = int(x - base * int(x / base))
		result = chr(ord('0') + n) + result if n < 10 else chr(ord('A') + n - 10) + result
		x = int(x / base)
	return True, result

from_base = 2
to_base = 12
x = '11101'
decode, result = convert_to_base_10(x, from_base)
if decode:
	code, y = convert_from_base_10(result, to_base)
	if code:
		print("{} in base {} = {} in base {}".format(x, from_base, y, to_base))
	else:
		print("Error in converting from base 10 into base {}".format(to_base))
else:
	print("Error in converting from base {} into base 10".format(from_base))