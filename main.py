from CPUClass import CPU

initCpu = CPU()

print("Hi welcome to the Arithmetic CPU where you can send out mathematically instructions to a fake python CPU. So exciting right?")
print("To start trying adding a variable to the memory: store store1 10")
instruction = input(
    "Please enter your instructions, if you're lost please read the read me!\n")


try:
    initCpu.controlUnit(instruction)
except Exception as e:
    if str(e) == "Invalid length of instruction":
        instruction = input(
            "Invalid length of instruction please read the read me and try again\n")
        initCpu.controlUnit(instruction)
    else:
        raise Exception(e)
