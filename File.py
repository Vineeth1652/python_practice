file=open("myfile.txt",'w')

file.write("Hi heelo ela unnav .. ")
file.close()

file=open("myfile.txt",'a')
file.write(" Will see you soon")
file.close()

file=open("myfile.txt",'r')
print(file.read())
file.close()

#Rename and removing files
import os
os.getcwd()
os.rename("myfile.txt","newFile.txt")
os.remove("your file name")

#Mangaing direcories
os.mkdir("give your path of direct")


