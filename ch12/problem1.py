filename=["1.txt","2.txt","3.txt"]
for file in filename:
    try:
        with open(file, 'r') as f:
            print(f"Open {file} successfully! ")
    except FileNotFoundError:
        print(f"File {file} not found!")