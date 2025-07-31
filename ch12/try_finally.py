def main():
    try:
       n=int(input("Enter a number: "))
       print(n)
       return
    except Exception as e:
        print(e)
        return
    finally:
       print("Thank You! ")
main()
