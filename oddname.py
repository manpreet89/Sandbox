__author__ = 'JC443852'
"""
    manpreet

"""
valid = False
while not valid:
 name = input(" enter your name:")
 if name != "" and not name.isspace():
    valid = True

l = len(name)
for i in range(0,l,2):
    print(name[i])
