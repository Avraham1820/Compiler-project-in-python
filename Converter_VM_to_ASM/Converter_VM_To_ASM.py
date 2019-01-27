#Avraham Shaharabani 032472664
#Daniel Lictenshtat  302026059

import os
import Comp_
import File_
import String_
import Decoding_
import INIT_
import Flow_

#globals vars
labelCounter= 0
currentClass=''
AsmStringOfFolder= ''
currentFunction = ''

def convert_VmString_To_AsmString(vmOfFile): # get string in VM and return string in ASM
    global AsmStringOfFolder
    for vmOrder in vmOfFile.splitlines():
        vmOrder = vmOrder.strip()
        if vmOrder != '':
            AsmStringOfFolder += convert_VmOrderStr_To_AsmOrdersStr(vmOrder)
    

def convert_VmOrderStr_To_AsmOrdersStr(vmOrder):
    global currentClass
    global currentFunction
    word0 = ''
    word1 = ''
    word2 = ''
    if len(vmOrder.split())> 0:
       line = vmOrder.split()
       word0 = ''.join(line[0:1])  #[pop] -> 'pop'
       if   len(vmOrder.split()) > 1:
            word1 = ''.join(line[1:2])
       if len(vmOrder.split()) > 2:
            word2 = ''.join(line[2:3])
       if word0=='eq' or word0=='gt' or word0=='lt' or word0=='call':
           global labelCounter
           labelCounter+=1
       if word0=='function':
           currentFunction = word1
    return  Decoding_.order(word0, word1, word2 ,labelCounter,currentClass,currentFunction)



def convertFilesInFolderToASM(folderPath): # path of folder  'Source'
    print 'hi'
    indexOfSlash = folderPath.rfind("\\")
    folderName = folderPath[indexOfSlash + 1:]

    if folderName == "StaticsTest" or folderName == "FibonacciElement":
        global labelCounter
        global AsmStringOfFolder
        AsmStringOfFolder += INIT_.sys_()
        AsmStringOfFolder += Flow_.call_('Sys.init', '0', labelCounter)

    #AsmStringOfFolder += INIT_.segments_(256, 300, 350, 400, 450)
    for root, dirs, files in os.walk(folderPath):  # scan the files in the folder 'Source'
        for file in files:
            fName = File_.getFileName(file)  # example :   fName ='SimpleAdd.vm'
            if fName.find('.vm') != -1:
                filePath = folderPath + '\\' + fName
                VmString = File_.convertFileToString(filePath)

                index = fName.find('.')
                fNameNoSuffix = fName[0:index]

                global currentClass
                currentClass = fNameNoSuffix
                vmOfFile=String_.getCleanCode(VmString)
                convert_VmString_To_AsmString(vmOfFile)
        projectFilePath = folderPath + '\\' +  folderName + '.asm'
        File_.make_File_From_String_(AsmStringOfFolder,projectFilePath)
    AsmStringOfFolder = ''   # we need to reset the globals vars if we want to run more than one projects
    currentClass = ''
    labelCounter = 0

def mainf():
    print "Enter a folder path:",
    folderPath = raw_input()
    if os.path.exists(folderPath):
       convertFilesInFolderToASM(folderPath)
    else:
       print 'The path : %s is not exsist'%folderPath

def mainf_(folderPath):
    if os.path.exists(folderPath):
       convertFilesInFolderToASM(folderPath)
    else:
       print 'The path : %s is not exsist'%folderPath


#mainf()


mainf_('C:\XXX_Python\Converter_VM_to_ASM\StackArithmetic\StackTest')

mainf_('C:\XXX_Python\Converter_VM_to_ASM\FunctionCalls\StaticsTest')
mainf_('C:\XXX_Python\Converter_VM_to_ASM\FunctionCalls\FibonacciElement')
mainf_('C:\XXX_Python\Converter_VM_to_ASM\FunctionCalls\SimpleFunction')

mainf_('C:\XXX_Python\Converter_VM_to_ASM\ProgramFlow\BasicLoop')
mainf_('C:\XXX_Python\Converter_VM_to_ASM\ProgramFlow\FibonacciSeries')


#mainf_('C:\XXX_Python\Converter_VM_to_ASM_2.25\haratsa al ratuv')
