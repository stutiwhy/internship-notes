ch = 0
while ch != 5:
    try:
        def add(x, y):
            return x + y
        def sub(x, y):
            return x - y
        def mul(x, y):
            return x * y 
        def div(x, y):
            return x / y 
        
        print("Enter 2 numbers : ")
        x = int(input())
        y = int(input())
        
        ch = int(input("Enter choice : "))

        if ch == 1:
            print(add(x, y))
        if ch == 2:
            print(sub(x, y))
        if ch == 3:
            print(mul(x, y))
        if ch == 4:
            print(div(x, y))

    except ZeroDivisionError as z:
        print("Cannot divide any number by zero.")
    except:
        print("Invalid inputs.")