temperatures=[10,-20,-289,100]

def celsius_to_farenheit(tempo):
    if tempo > -256:
        farenheit=tempo*9/5+32
        return farenheit
    else:
#            farenheit=temp*9/5+32
        print("Incorrect")

#            print(celsius_to_farenheit(farenheit))
for tempo in temperatures:
    inform=celsius_to_farenheit(tempo)
    print(inform)
    if inform is not None:
        file = open("testfile.txt","a")
        file.write(format(inform)+ '\n')
        file.close()
    else:
        print("NAda")
