import os
import datetime

current_time=(datetime.datetime.now()).strftime("%Y-%m-%d-%H-%M-%S-%f")

print(current_time)
write_file = open("temp/"+(current_time)+".txt", "w")

dir = "Sample-Files"
list = os.listdir(dir)
number_files = len(list)
print number_files

for i  in xrange(number_files): #number_files:
    i = i+1
    read_file = open("Sample-Files/file"+str(i)+".txt", 'r').read()
    print(float(i))
    print(read_file)
    write_file.write(read_file+"\n")

write_file.close()

#Solucion
#import glob2
#import datetime

#filenames=glob2.glob("*.txt")

#with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
#    for filename in filenames:
#        with open(filename,"r") as f:
#            file.write(f.read()+"\n")
