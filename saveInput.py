def execute(userInput):
    txt = ".txt"
    directory = "/Save/" + userInput + "{}".format(txt)
    fileWorking = False
    while not (fileWorking):
        try:
            open(directory, "r")
            fileWorking = True
        except:
            open(directory, "w")
            fileWorking = False
    fileRead = open(directory, "r")
    data = fileRead(0)
    amountUsed = data[0].strip()
    intAmountUsed = int(amountUsed)
    fileRead.close()
    intAmountUsed + 1
    fileWrite = open(directory, "w")
    file.writelines(intAmountUsed)
    fileWrite.close()
    
            