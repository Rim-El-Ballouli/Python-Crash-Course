def make_album(name, title, tracks=''):
    dict = {'name': name, 'title': title}
    if tracks:
        dict['tracks'] = tracks
    return dict

while True:
    print('Enter q any time to quit')

    n = input('Enter artist name ')
    if n == 'q':
        break

    t = input('Enter album title ')
    if t == 'q':
        break

    print(make_album(n,t))
