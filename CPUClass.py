
class CPU:
    def __init__(self, memoryLength=16):
        self.memoryLength = memoryLength
        self.memory = [None]*memoryLength
        self.cacheLength = memoryLength // 4
        self.cache = [[None, None]] * self.cacheLength

    def controlUnit(self, instruction):
        print("Preparing instruction for processing")

        # Oh yeahhhh you can chain commands
        if ';' in instruction:
            instructionArray = instruction.split(";")
            for text in instructionArray:
                self.controlUnit(text)
            return self.memory

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
            return self.ALU(instructionArray[0], instructionArray[1],
                            instructionArray[2], instructionArray[3])

    def ALU(self, op, val1, val2, store):
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
            self.memoryUnit("store", val2, val1)
            return self.memory
        elif "retrieve" == op:
            return self.memoryUnit("retrieve", val1)
        elif "del" == op:
            self.memoryUnit("del", val1)
            return self.memory
        else:
            raise Exception("Invalid instruction")

        if op[-1] == "s":
            self.memoryUnit("store", store, result)
            return self.memory
        else:
            return result

    def memoryUnit(self, insturction, store, val=None):
        print("Accessing memory unit")

        if insturction == "store":
            cacheAddress = self.getCacheAddress(store)
            self.cache[cacheAddress] = [store, int(val)]
            self.memory[int(store) - 1] = int(val)
            print(f"Successfully stored result in {store}")
        elif insturction == "retrieve":
            print(f"Retrieving data from {store}")
            cacheAddress = self.getCacheAddress(store)
            cacheVal = self.cache[cacheAddress]
            if cacheVal[0] == store:
                return cacheVal[1]
            else:
                var = self.memory[int(store) - 1]
                self.cache[cacheAddress] = [store, var]
                if var == None:
                    raise Exception("No variable")
                return var
        elif insturction == "del":
            cacheAddress = self.getCacheAddress(store)
            self.cache[cacheAddress] = [None, None]
            self.memory[int(store) - 1] = None
            print(f"Successfully deleted data from {store}")
        else:
            raise Exception("Invalid instruction")

    def getCacheAddress(self, store):
        print("Checking the cache")
        if int(store) > 0 and int(store) <= 4:
            return 0
        elif int(store) > 4 and int(store) <= 8:
            return 1
        elif int(store) > 8 and int(store) <= 12:
            return 2
        elif int(store) > 13 and int(store) <= 16:
            return 3
        else:
            raise Exception("Invalid Store")
