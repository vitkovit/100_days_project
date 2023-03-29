# %% Functions with outputs
def format_name(f_name, l_name):
    #     print(f_name.title())
    #     print(l_name.title())
    return (f_name.title(), l_name.title())


format_name("who aRe", "you")


# %%
def format_name2(f_name, l_name):
    """Teake something and do bla bla bla"""
    # this is how you type docstring
    #     print(f_name.title())
    #     print(l_name.title())
    if f_name == "" or l_name == "":  # you can have multiple returns
        return "you suck"
    return (f_name.title(), l_name.title())


format_name2(input("what is your name: "), input("what is your lame name: "))

# %% Exercise 1 - Days in Month


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
# %%103. Calculator Part 1: Combining Dictionaries and Functions

#Calculator
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

# %%
