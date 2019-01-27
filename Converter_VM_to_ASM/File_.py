import os

def getFileName(file):###Good
  fName = str(os.path.join(file))  # the name of the file
  fName.strip()  # to clean the spacelines on the sides of the string
  return  fName  # return  'SimpleAdd.vm'

def convertFileToString(filePath):  ###Good
    #print filePath
    #return 'k'
    file = open(filePath, 'r')  # Open a stream to read the file
    content = file.read()  # Read from the file all the text to a var
    file.close()  # Close the stream
    return content


def make_File_From_String(AsmString, folderName, ToFileType, FolderPath):  # path of the folder
    FileNameWith_End = folderName + ToFileType
    newPath = FolderPath + '/' + FileNameWith_End  # for creating the new file we need new path
    opened_file = open(newPath, 'w')  # Open a stream to write on the file
    opened_file.write(AsmString)
    opened_file.close()

def make_File_From_String_(string1, filePath):  # path of the folder
    #print filePath
    #return
    opened_file = open(filePath, 'w')  # Open a stream to write on the file
    opened_file.write(string1)
    opened_file.close()