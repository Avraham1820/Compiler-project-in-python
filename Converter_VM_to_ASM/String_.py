def getCleanCode (code):
    cleanCode =''
    for line in code.splitlines():
        indexOfComment = line.find('//')
        if  indexOfComment == -1:
            cleanCode += (line.strip() + '\n')
        elif indexOfComment > 0: # so in the begin of the line there is an order
            line = line[0:indexOfComment]
            cleanCode += (line.strip() + '\n')
        #elif indexOfComment == 0:
        #    cleanCode += (line.strip() + '\n')
    return  cleanCode


