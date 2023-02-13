def computepay(h, r):
    if h > 40 :
        return ((40 * r) + ((h-40) * r * 1.5))
    else :
        return (h * r)

hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
try :
    fh = float(hrs)
    fr = float(rate)
except :
    print("Error! Please enter the values in numeric form")
    quit()
p = computepay(fh, fr)
print("Pay", p)
