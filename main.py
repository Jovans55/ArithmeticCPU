from CPUClass import CPU

initCpu = CPU()

print("Hi welcome to the Arithmetic CPU where you can send out mathematically instructions to a fake python CPU. So exciting right?")
print("To start trying adding 10 to the memory address 1: store 10 1")
print("TO EXIT PLEASE TYPE: BYE")


def runControlUnit():
    instruction = input(
        "Please enter your instructions, if you're lost please read the read me!\n")

    if instruction.lower() == "bye":
        quit()

    # A lot of error handling to prevent many things from going wrong and giving the user feedback.
    try:
        result = initCpu.controlUnit(instruction)
    except Exception as e:
        if str(e) == "Invalid length of instruction":
            instruction = input(
                "Invalid length of instruction please read the read me and try again\n")
            runControlUnit()
        elif str(e) == "Invalid instruction":
            instruction = input(
                "Invalid instruction please read the read me and try again\n")
            runControlUnit()
        elif str(e) == "Divied by zero":
            instruction = input(
                "Divied by zero please pick a different store or store a none zero variable\n")
            runControlUnit()
        elif str(e) == "Invalid Store":
            instruction = input("Invalid store address! please try again\n")
            runControlUnit()
        elif str(e) == "No variable":
            instruction = input(
                "No variable stored there! Please store one or try a different store\n")
            runControlUnit()
        elif isinstance(e, ValueError) and "invalid literal for int()" in str(e):
            instruction = input(
                "Invalid input: expected a number but got a string or float/decimal. Please try again.\n")
            runControlUnit()
        else:
            raise Exception(e)
    print(result)
    runControlUnit()


runControlUnit()
