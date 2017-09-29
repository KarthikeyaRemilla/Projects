
def calculator():
    print("Hello! Welcome to Py Calculator. Following operators are available for you: \n 1. Addition(+) 2. Subtraction(-) 3. Multiplication (*) 4. Division(/) 5. Remainder(%)")
    choice = int(input("Enter your choice now: "))
    a = float(input("Enter operand a : "))
    b = float(input("Enter operand b : "))
    result = float(0)
    decision = 'y'
    do while(decision == 'y' or decision == 'Y'):
        if (choice == 1):
            result = a + b 
            print("Sum is %f" %result)
        elif (choice ==2):
            result = a - b 
            print("Difference is %f" %result)
        elif (choice ==3):
            result = a * b
            print("Product is %f" %result)
        elif (choice == 4):
            result = a/b    
            print("Quotient of division is %f" %result)
        else:
            result = a%b 
            print("Remainder of division is %f" %result)
        decision = str(input("Press 'y/Y' to continue or 'q/Q' to exit:"))
        if(decision == 'q' or decision == 'Q'):
            print("Goodbye")

calculator()        
    
        
        
     