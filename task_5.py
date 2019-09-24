import sys


def palindroms(length):
	count = []
	for num in range(length+1):
		if len(str(num))>1:
			dig_1 = num // 10
			dig_2 = num % 10
			if dig_1 == dig_2:
				count.append(num)
	return count

def main():
	try:
		length = int(input('Enter length of sequence: '))
		if 0 < length <= 100:
			text = "Numbers palindromes in the sequence: "
			nums_palindroms = palindroms(length)
			if nums_palindroms:
				for number in nums_palindroms:
					text += str(number) + ", "
				text = text[0:-2] + "."
				print(text)
			else:
				print('There are no numbers palindromes')
			sys.exit(0)			
		elif length <= 0:
			print('Length of sequence must be positive')
		elif length > 100:
			raise ValueError
	except ValueError:
		print('Please, enter an integer number less or equal 100')

if __name__ == '__main__':
	while True:
		main()
