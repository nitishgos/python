with open("this.txt","r") as f:
    lines=f.readlines()
lineno=1
for line in lines:
        if("python" in line.lower()):
            print(f"Python is present in word. line no is {lineno}")
            break
        lineno+=1
else:
     print("Python is not present in the file")