with open("this.txt","r") as f:
    content1=f.read()
with open("copy.txt","r") as f:
    content2=f.read()
if(content1==content2):
    print(" The file is identical & matches the content of another file.")
else:
    print("The file is not identical & does not match the content of another file.")