num1= int(input())
num2= int(input())
op= input("choose operator  * / // :")

match op:
    case "+":
        result= num1+num2
        print("result of the + operation is :", result)
    case "*":
        result= num1*num2
        print("result of the * operation is :", result)
    case "/":
        result= num1/num2
        print("result of the / operation is :", result)
    case _:
        print("invalid operator")