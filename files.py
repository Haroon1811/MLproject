fo  = open("foo.txt", "wb")
print("name of the file :", fo.name)
print("closed or not :", fo.closed)
print("opening mode :", fo.mode)
#rint("Softspace flag :", fo.softspace)


file = open("test.txt", "w")
file.write("new text file created.")
file.close()


file = open("test.txt", "r")
print(file.read())
file.close()


file=open("test.txt", "a")
file.write("new line appended")
file.close()

f = open("business.csv", "r")
print(f.read())
f.close()