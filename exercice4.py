c=[10,-20,-289,100]

def c_to_f(number):
    if number < -273:
        return("Imposible!")
    else:
        f=number*9/5+32
        return f
#print(c_to_f(10))

#c = float(input("Enter your temperature"))
for number in c:
    print"Your temparature in celsius",",",(c_to_f(number))
