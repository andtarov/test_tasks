import sys


def gcd(num_1, num_2):
	while num_2:
		num_1, num_2 = num_2, num_1%num_2
	return abs(num_1)


def lcm(num_1, num_2):
	return int((num_1/gcd(num_1, num_2))*num_2)


def main():
	try:
		number_1 = int(input ('Enter first number: '))
		number_2 = int(input ('Enter second number: '))
		if number_1 and number_2:
			gcd_of_nums = gcd(number_1, number_2)
			lcm_of_nums = lcm(number_1, number_2)
			print(f"Greatest common divisor of {number_1} and {number_2} is {gcd_of_nums}")
			print(f"Least common multiple of {number_1} and {number_2} is {lcm_of_nums}")
			sys.exit(0)
		else: 
			print('Please, enter numbers distinct from zero')
	except ValueError:
		print('You entered uncorrect value!')


if __name__ == '__main__':
	while True:
		main()
