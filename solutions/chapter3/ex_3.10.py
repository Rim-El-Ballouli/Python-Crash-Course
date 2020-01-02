list = ['element1', 'element2', 'element3', 'element4', 'element5']
print("This list include " + str(len(list)) + " elements\n")

print("You can add elements in two ways using append() and insert()")
list.insert(len(list), 'element6') #insert at position
list.append('element7') #insert  at the end of list
print('This list now is')
print(list)
print('\n')

print("You can delete elements in a list in four ways using pop() and del and remove()")
list.pop() # remove and return last element in list
del list[len(list)-1] #delete element at index
list.pop(len(list)-1) #delete element at index
list.remove('element1') #remove element by value
print('This list now is')
print(list)
print('\n')

print("You can sort a list in two ways using sorted() and sort")
sorted(list) #sort without modifying the original list
list.sort() #sort and modify the original list
print('This list now is')
print(list)
print('\n')

print("You can sort a list in reverse order in two ways using sorted() and sort")
sorted(list, reverse=True) #sort without modifying the original list
list.sort(reverse=True) #sort and modify the original list
print('This list now is')
print(list)
print('\n')