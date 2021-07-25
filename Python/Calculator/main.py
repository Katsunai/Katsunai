# CALCULATOR [SIMPLE NO GUI EDITION]
# CREATED BY : KATSUNAI
# VERSION : 1.0.0
# LICENSE : MIT LICENSE


def Calculate():
    # Required Variables
    Operator = None
    Number_1 = 0
    Number_2 = 0
    TotalVal = 0
    RunTime = None

    # User Input For Calculation
    Number_1 = int(input("Number: "))
    Operator = input("Operator: ")
    Number_2 = int(input("Number: "))

    if Operator == "+":
        TotalVal = Number_1 + Number_2
    elif Operator == "-":
        TotalVal = Number_1 - Number_2
    elif Operator == "x":
        TotalVal = Number_1 * Number_1
    elif Operator == "/":
        TotalVal = Number_1 / Number_2

    print(f"Total Value: {TotalVal}")
