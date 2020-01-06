sandwich_orders = [ 'pastrami', 'tuna', 'cheese', 'pastrami', 'ham', 'egg', 'pastrami']
finished_sandwiches = []

print('deli has run out of pastrami')
while 'pastrami' in sanwich_orders:
	sandwich_orders.remove('pastrami')
	
while sandwich_orders:
	curr = sandwich_orders.pop()
	finished_sandwiches.append(curr)
	print('I made your ' + curr +  ' sandwich')

print('Finished sandwishes are:')
print(finished_sandwiches)
print('sandwich orders are:')
print(sandwich_orders)
