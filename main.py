#calculator
#add
def add(n1,n2):
    return n1 + n2
#subtract
def subtract(n1,n2):
    return n1 - n2
#multiply
def multiply(n1,n2):
    return n1 * n2
#division
def division(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/": division,
}
num1 = int(input("Enter the first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Enter the operation: ")
num2 = int(input("Enter the second number: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("Enter the third number: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

third_answer = True
while third_answer:
    next_part = input(f"Type 'y' to continue calculating with 8, or type 'n' to exit: ")
    if next_part == 'y':
        operation_symbol = input("Pick an operation: ")
        num4 = int(input("Enter the fourth number: "))
        calculation_function = operations[operation_symbol]
        third_answer = calculation_function(second_answer, num4)
        print(f"{second_answer} {operation_symbol} {num4} = {third_answer}")
        break
    elif next_part == 'n':
        third_answer = False
        print("Exiting...")
    else:
        print("Invalid input.")