from art import logo
# Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiple
def multiple(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide,
}
def calculator():
    print(logo)
    should_continue = True
    num1 = int(input("first number: "))
    for symbol in operations:
        print(symbol)


    while should_continue == True:
        opr_sym = input("pick an operation: ")
        opr_fun = operations[opr_sym]
        num2 = int(input("second number: "))
        anwser = opr_fun(num1, num2)

        print(f"{num1} {opr_sym} {num2} = {anwser}")
        if input(f"trype (y) to continue calculation wiht {anwser}: or (n) to start new calculation") == "y":
            num1 = anwser
        else:
            should_continue = False
            calculator()
        # opr_sym = input("pick another operation: ")
        # num3 = int(input("next number: "))
        # opr_fun = operations[opr_sym]
        # second_anwser = opr_fun(anwser, num3)

        # print(f"{anwser} {opr_sym} {num3} = {second_anwser}")

calculator()