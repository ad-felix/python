s = input("Enter a string: ")
if len(s) < 3 :
    print(s)
else:
    if s[-3:] == 'ing':
        s += 'ly'
        print(s)
    else:
        s += 'ing'
        print(s)
