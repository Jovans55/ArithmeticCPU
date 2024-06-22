
class CPU:
    def __init__(self, memoryLength=16):
        # memory length must be in multiples of 4 cause I said so
        self.memoryLength = memoryLength
        self.memoryUnit = []

        # if you want the memory to be multiples of anything else just change this first
        self.cacheLength = memoryLength // 4
        self.cache = [[]] * self.cacheLength

    def controlUnit(self, instruction):
        print("Preparing instruction for processing")
        instructionArray = instruction.split()
        if len(instructionArray) > 4 or len(instructionArray) < 2:
            raise Exception("Invalid length of instruction")
        else:
            while len(instructionArray) < 4:
                instructionArray.append(None)
            self.ALU(instructionArray[0], instructionArray[1],
                     instructionArray[2], instructionArray[3])

    def ALU(self, op, val1, val2, store):
        print("Starting arithmetic & logic unit")
        print(op, val1, val2, store)
