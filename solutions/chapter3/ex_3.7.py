invites = ['Person1', 'Person2', 'Person3', 'Person4']
print('Mr./Mrs. ' + invites[0] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[1] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[2] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[3] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')


print('\n Unfortunately, Mr./Mrs. ' + invites[1] + " can't make")
invites[1] = 'New-Person'

print('Mr./Mrs. ' + invites[0] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[1] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[2] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[3] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')

print('\n Horray!!!, found a bigger table, can invite more people')
invites.insert(0, 'Person5')
invites.insert(2, 'Person6')
invites.append('Person7')


print('Mr./Mrs. ' + invites[0] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[1] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[2] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[3] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[4] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[5] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[6] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')

print('\n  Unfortunately, the table will not arrive on time' +
      'Therefore can invite only two people for dinner.')
print('Sorry can’t invite Mr./Mrs. ' + invites.pop())
print('Sorry can’t invite Mr./Mrs. ' + invites.pop())
print('Sorry can’t invite Mr./Mrs. ' + invites.pop())
print('Sorry can’t invite Mr./Mrs. ' + invites.pop())
print('Sorry can’t invite Mr./Mrs. ' + invites.pop())


print('\n Mr./Mrs. ' + invites[0] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')
print('Mr./Mrs. ' + invites[1] + ' we are thrilled to inform you '
                                 'that you are invited to our special dinner')

del invites[0]
del invites[1]

print(invites)