print("Welcome system press 'm' for exit.")
b = 1
while True:
    a = input("Please enter the number for which you want to find the factorial:")
    if a == "m":
        break
    else:
        a = int(a)
        b = 1

        for i in range(2, a+1):
            b *= i

        print(b)
