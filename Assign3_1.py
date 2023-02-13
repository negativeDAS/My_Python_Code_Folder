hrs = input('Enter hours')
rate = input('Rate per hour')
try :
    h = float(hrs)
    r = float(rate)
except :
    print("Error! Please, enter the numeric input")
    quit()

ovrtme = (40 * r) + ((h-40) * r * 1.5)

if h <= 40 :
    print(h*r)

else :
    print(ovrtme)
