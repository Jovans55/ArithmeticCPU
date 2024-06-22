from CPUClass import CPU

initCpu = CPU()

print("Hi welcome to the Arithmetic CPU where you can send out mathematically instructions to a fake python CPU. So exciting right?")
print("To start trying adding 10 to the memory store 1: store 10 store1")
instruction = input(
    "Please enter your instructions, if you're lost please read the read me!\n")

try:
    print(initCpu.controlUnit(instruction))
except Exception as e:
    if str(e) == "Invalid length of instruction":
        instruction = input(
            "Invalid length of instruction please read the read me and try again\n")
        print(initCpu.controlUnit(instruction))
    elif str(e) == "Invalid instruction":
        instruction = input(
            "Invalid instruction please read the read me and try again\n")
        print(initCpu.controlUnit(instruction))
    elif str(e) == "Divied by zero":
        instruction = input(
            "Divied by zero please pick a different store or restore a none zero variable\n")
        print(initCpu.controlUnit(instruction))
    elif str(e) == "Invalid Store":
        instruction = input("Invalid Store! please try again\n")
        print(initCpu.controlUnit(instruction))
    else:
        raise Exception(e)
