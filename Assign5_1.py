user_inp = input('Enter a number')
largest = None
smallest = None
while True :
    if user_inp == 'done' :
        ilargest = int(largest)
        ismallest = int(smallest)
        print('Maximum is',ilargest)
        print('Minimum is',ismallest)
        break
    else :
        try:
            fuser_inp = float(user_inp)
        except:
            print('Invalid input')
        if largest is None :
            largest = fuser_inp
        elif fuser_inp > largest :
            largest = fuser_inp
        if smallest is None :
            smallest = fuser_inp
        elif fuser_inp < smallest :
            smallest = fuser_inp
        user_inp = input('Enter a number: ')
