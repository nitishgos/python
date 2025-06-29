with open("this.txt","r") as f:
    content=f.read()
if("python" in content.lower()):
    print("Python is mentioned in the file")
else:
    print("Python is not mentioned in the file")