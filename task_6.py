from collections import namedtuple
import sys


Thing = namedtuple('Thing', 'cost weight')

def create_thing(num):
	while True:
		try:			
			cost = float(input(f'Enter cost of {num} thing: '))
		except ValueError:
			print('Please enter a NUMBER!')
		else:
			while True:
				try:
					weight = int(input(f'Enter weight of {num} thing: '))
				except ValueError:
					print('Please enter an NATURAL NUMBER!')
				else:
					item = Thing(cost, weight)
					return item


def best_cost(num_things, weight_limit):
	if num_things == 0:
		return 0
	elif things[num_things - 1].weight > weight_limit:
		return best_cost(num_things - 1, weight_limit)
	else:
		return max(
			best_cost(num_things - 1, weight_limit),
			best_cost(num_things - 1, weight_limit - things[num_things - 1].weight) + 
			things[num_things - 1].cost
			)

def main():
	global things
	things = []
	total_things = []
	total_cost = 0
	total_weight = 0
	try:
		amount_of_things = int(input('Enter amount of things: '))
		if amount_of_things:
			for num in range(1, amount_of_things+1):
				thing = create_thing(num)
				things.append(thing)
			while True:
				try:
					capacity = int(input('Enter capacity of the bag: '))
					break
				except ValueError:
					print('Please enter a NATURAL NUMBER!') 
		else:
			raise ValueError
	except ValueError:
		print('Please enter a NATURAL number!')
	else:
		for i in reversed(range(len(things))):
			if best_cost(i+1, capacity) > best_cost(i, capacity):
				total_things.append(things[i])
				capacity -= things[i].weight
		for th in total_things:
			total_cost += th.cost 
			total_weight += th.weight
		print(f'For the maximum cost {total_cost}cu you should take things: {total_things}. Total weight is {total_weight}cu.')
		sys.exit(0)



if __name__ == '__main__':
	while True:
		main()
