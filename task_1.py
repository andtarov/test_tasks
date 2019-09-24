import sys


def even_or_odd(num):
	if num%2 == 0:
		return 'even'
	else:
		return 'odd'


def simple_or_composite(num):
	count = 0
	for i in range(1, num+1):
		if num%i == 0:
			count +=1
	if count > 2:
		return 'composite'
	else:
		return 'simple'


def main():		
	try:
		number = int(input('Enter an integer number: '))
		if number >= 0:
			parity = even_or_odd(number)
			if number > 1:
				simplicity = simple_or_composite(number)
				print(f"Number {number} is {simplicity} and {parity}")
			else:
				print(f"Number {number} is {parity} and not simple or composite")
			sys.exit(0)
		else:
			print('Please, enter an NATURAL number!') 
	except ValueError:
		print('Please, enter an INTEGER NUMBER!')
	

if __name__ == '__main__':
	while True:	
		main()
		