favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

names = ['jen', 'sarah', 'Danny', 'Albert']

for name in names:
    if name in favorite_languages.keys():
        print('Thank you for talking the pool')
    else:
        print('Please take the pool')


