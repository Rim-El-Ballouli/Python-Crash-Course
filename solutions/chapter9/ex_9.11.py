# change file name of ex_9.8 to ex_9_8
# module names shouldnt contain _
from ex_9_8 import Admin

usrAdmin = Admin('Adrean', 'Park', "can add post", "can delete post", "can ban user")
usrAdmin.privileges.show_privileges()