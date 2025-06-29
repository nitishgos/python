f=open("this.txt")
# data=f.readlines()
# print(data)
# data1=f.readline()
# print(data1)
# data2=f.readline()
# print(data2)
# data3=f.readline()
# print(data3)
line = f.readline()
while line != "":
    print(line, end="")  # end="" prevents extra newlines
    line = f.readline()
f.close()