scr = input('Enter Score: ')
try  :
    fscr = float(scr)
except :
    print("Error! : Please Enter the score in Numeric form")
    quit()


if (fscr >= 0.0) and (fscr <= 1.0) :
    if fscr >= 0.9 :
        print('A')
    elif fscr >= 0.8 :
        print('B')
    elif fscr >= 0.7 :
        print('C')
    elif fscr >= 0.6 :
        print('D')
    elif fscr < 0.6 :
        print('F')
else :
    print("The score is either less than 0 or greater than 1")
