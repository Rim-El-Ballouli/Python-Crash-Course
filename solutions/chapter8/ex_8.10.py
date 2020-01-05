def show_magicians(listmag):
    for magician in listmag:
        print(magician)
    
def make_great(list):
	for i in range(len(list)):
		list[i] = 'Great ' + list[i]
		
list_magicians = ['Eric', 'Tom', 'Nancy']
make_great(list_magicians)
show_magicians(list_magicians)
