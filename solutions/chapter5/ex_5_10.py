current_users = ['tony', 'eric', 'mart', 'sindy']
new_users = ['Julie', 'Lina', 'Mart', 'Sindy']

for user in new_users:
    if user.lower() in current_users:
        print('You will need to enter a new username')
    else:
        print('User name is available')
