
class CPU:
    def __init__(self, memoryLength=16):
        self.memoryLength = memoryLength
        self.memory = [None]*memoryLength
        self.cacheLength = memoryLength // 4
        self.cache = [[None, None]] * self.cacheLength

    def controlUnit(self, instruction):
        print("Preparing instruction for processing")
        instructionArray = instruction.split()

        if "showMem" == instructionArray[0]:
            return self.memory
        elif "showCache" == instructionArray[0]:
            return self.cache

        if len(instructionArray) > 4 or len(instructionArray) < 2:
            raise Exception("Invalid length of instruction")
        else:
            while len(instructionArray) < 4:
                instructionArray.append(None)
            self.ALU(instructionArray[0], instructionArray[1],
                     instructionArray[2], instructionArray[3])

    def ALU(self, op, val1, val2, location, store):
        print("Starting arithmetic & logic unit")

        # I used (if in) here before but I think this is more optimized and stops stuff like addiuigs from passing
        if "add" == op or "adds" == op:
            var1 = self.memoryUnit("retrieve", val1)
            var2 = self.memoryUnit("retrieve", val2)
            result = var1 + var2
        elif "sub" == op or "subs" == op:
            var1 = self.memoryUnit("retrieve", val1)
            var2 = self.memoryUnit("retrieve", val2)
            result = var1 - var2
        elif "div" == op or "divs" == op:
            var1 = self.memoryUnit("retrieve", val1)
            var2 = self.memoryUnit("retrieve", val2)

            if var1 == 0 or var2 == 0:
                raise Exception("Divied by zero")

            result = var1 / var2
        elif "mul" == op or "muls" == op:
            var1 = self.memoryUnit("retrieve", val1)
            var2 = self.memoryUnit("retrieve", val2)
            result = var1 * var2
        elif "store" == op:
            self.memoryUnit("store", store, val1)
        elif "retrive" == op:
            self.memoryUnit("retrive", val1)
        elif "del" == op:
            self.memoryUnit("del", val1)
        else:
            raise Exception("Invalid instruction")

        if op[-1] == "s":
            self.memoryUnit("store", result, location)

    def memoryUnit(self, insturction, store, val=None):
        print("Accessing memory unit")

        if insturction == "store":
            print(f"Successfully stored result in {store}")
        elif insturction == "retrieve":
            print("Checking the cache")
            if int(store[-1]) > 0 and int(store[-1]) <= 4:
                cacheVal = self.cache[0]
            elif int(store[-1]) > 4 and int(store[-1]) <= 8:
                cacheVal = self.cache[1]
            elif int(store[-1]) > 8 and int(store[-1]) <= 12:
                cacheVal = self.cache[2]
            elif int(store[-1]) > 13 and int(store[-1]) <= 16:
                cacheVal = self.cache[3]
            else:
                raise Exception("Invalid Store")
            print(f"Retrieving data from {store}")
        elif insturction == "del":
            print(f"Checking the cache in case {
                  store} data resides there as well")
            if int(store[-1]) > 0 and int(store[-1]) <= 4:
                cacheVal = self.cache[0]
            elif int(store[-1]) > 4 and int(store[-1]) <= 8:
                cacheVal = self.cache[1]
            elif int(store[-1]) > 8 and int(store[-1]) <= 12:
                cacheVal = self.cache[2]
            elif int(store[-1]) > 13 and int(store[-1]) <= 16:
                cacheVal = self.cache[3]
            else:
                raise Exception("Invalid Store")
            print(f"Successfully deleted data from {store}")
        else:
            raise Exception("Invalid instruction")
