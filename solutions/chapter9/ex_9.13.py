from collections import OrderedDict
glossary = OrderedDict()

glossary['keywords'] = 'words reserved for '
glossary['conditional'] = 'an expression that either evaluates to true or false, used to control flow in code '
glossary['dictonary'] = 'a key value pair of elements '
glossary['tuple'] = 'a list of elements  whose elements  can not be modified'
glossary['list'] = 'a list of elements that can be modified'
glossary['Loop'] = 'a way to change the control flow in the program to repeate a set of statments a number of times'

for key, value in glossary.items():
    print(key.title() + ': ' + value)