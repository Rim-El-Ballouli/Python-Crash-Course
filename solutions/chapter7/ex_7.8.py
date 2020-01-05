sandwich_orders = ['tuna', 'cheese', 'ham', 'egg']
finished_sandwiches = []

while sandwich_orders:
	curr = sandwich_orders.pop()
	finished_sandwiches.append(curr)
	print('I made your ' + curr +  ' sandwich')

print('Finished sandwishes are:')
print(finished_sandwiches)
print('sandwich orders are:')
print(sandwich_orders)