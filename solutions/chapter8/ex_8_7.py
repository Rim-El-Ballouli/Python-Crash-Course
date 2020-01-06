def make_album(name, title, tracks=''):
    dict = {'name': name, 'title': title}
    if tracks:
        dict['tracks'] = tracks
    return dict

print(make_album('Mini World','Indila'))
print(make_album('Mini World','Indila','10'))
