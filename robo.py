mm = input("Enter the path: ")
l = mm.count('L')
r = mm.count('R')
u = mm.count('U')
d = mm.count('D')

if 'L' in mm and 'U' in mm:
    if l == r and u == d:
        print('True')
    else:
        print('False')
elif 'L' in mm:
    if l == r:
        print("True")
    else:
        print("False")
else:
    if u == d:
        print("True")
    else:
        print("False")