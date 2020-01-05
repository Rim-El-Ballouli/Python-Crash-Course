def show_magicians(listmag):
    for magician in listmag:
        print(magician)
    
def make_great(list):
	for i in range(len(list)):
		list[i] = 'Great ' + list[i]
	return list
		
list_magicians = ['Eric', 'Tom', 'Nancy']
new_list = make_great(list_magicians[:])
show_magicians(list_magicians)
show_magicians(new_list)
