glossary = {
    'keywords' : 'words reserved for ',
    'conditional' : 'an expression that either evaluates to true or false, used to control flow in code',
    'dictonary' :  'a key value pair of elements',
    'tuple' : 'a list of elements  whose elements  can not be modified',
    'Loop' : 'a way to change the control flow in the program to repeate a set of statments a number of times',
    'list' : ' a list of elements that can be modified'
}

for key, value in glossary.items():
    print(key.title() + ': ' + value)