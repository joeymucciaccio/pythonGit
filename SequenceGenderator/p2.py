#Joseph Mucciaccio
#This program consists of requirements to demonstare the predator-prey example

import os


def openFile(fileName, mode):
    try:
        f = open(fileName, mode)
        return f
    except:
        print("Coud not open file {} with mode {}.".format(fileName, mode))
        f.close()

def writeToFile(filename, string):
    f = openFile(filename, "+w")
    f.write(string)
    f.close


def fileContentStr(fn):
    try:
        f = open(fn, "r")
        file_content = f.read()
        file_content_string = ""
        for i in file_content:
            file_content_string = file_content_string + i
  
        return file_content_string
    except:
        print("Error reading contents of the file.")


def ed_clear(filename):
    f = openFile(filename, "+w")
    f.write("")
    f.close()


def ed_read(filename, fromValue = 0, to = -1):
    file_content_string = fileContentStr(filename)
    lengthFileContent = len(file_content_string)
    if(fromValue > lengthFileContent):
        raise ValueError("Parameter exceeds the file length")
    if(to == -1):
        return(file_content_string[fromValue:])
    else:
        return(file_content_string[fromValue:to])

def ed_find(filename, search_str):
    listIndexesFound = []
    file_content_string = fileContentStr(filename)
    if(file_content_string is None):
        file_content_string = ""
    findIndex = file_content_string.find(search_str)
    if findIndex == -1:
        return listIndexesFound
    else:
        listIndexesFound.append(findIndex)
        while(findIndex != -1):
            findIndex = file_content_string.find(search_str, findIndex + len(search_str))
            if(findIndex != -1):
                listIndexesFound.append(findIndex)
    return listIndexesFound
  

def ed_replace(filename, search_str, replace_with, occurrence =- 1):
    stringContent = ed_read(filename)
    listIndexFound = ed_find(filename,search_str)
    if(occurrence == -1):
        replaceTimes = len(listIndexFound)
        stringContent = stringContent.replace(search_str,replace_with,replaceTimes)
    else:
        replaceTimes = 1
        if(occurrence >= len(listIndexFound)):
            return 0
        else:
            tempString = stringContent[0:listIndexFound[occurrence]]
            stringContent = stringContent[listIndexFound[occurrence]:].replace(search_str, replace_with, replaceTimes)
            stringContent = tempString + stringContent
  
    writeToFile(filename, stringContent)
    return replaceTimes


def ed_append(filename, string):
    length = len(string)
    f = openFile(filename, "a")
    f.write(string)
    f.close()
    return length


def ed_write(filename, pos_str_col):
    fileContentStr = ed_read(filename)
    totalLengthString = len(fileContentStr)
    for key,value in pos_str_col:
        if(key > totalLengthString):
            raise ValueError("Position parameter is grater than the file size at ", key)
        else:
            temp_string = fileContentStr[0:key]
            pos_string = value + fileContentStr[key + len(value):]
            fileContentStr = temp_string + pos_string
    writeToFile(filename, fileContentStr)
    return len(pos_str_col)
  

def ed_insert(filename, pos_str_col):
    fileContentStr = ed_read(filename)
    totalLengthString = len(fileContentStr)
    slicePos = 0
    for key, value in pos_str_col:
        if(key > totalLengthString):
            raise ValueError("Position parameter is grater than the file size at ", key)
        else:
            tempStr = fileContentStr[0:key + slicePos]
            posStr = value + fileContentStr[key + slicePos:]
            fileContentStr = tempStr + posStr
            slicePos = slicePos + len(value)
    writeToFile(filename, fileContentStr)
    return len(pos_str_col)


def ed_search(path, search_string):
    listNA = [".DS_Store"]
    listABS = []
    for dirname, dir_list, file_list in os.walk(path):
        for f in file_list:
            if f not in listNA:
                listIndexFound = ed_find(os.path.join(dirname, f), search_string)
                if len(listIndexFound) > 1:
                    listABS.append(os.path.join(dirname, f))
    return listABS

def test_ed_find(b, testname, msgOK="", msgFailed=""):
    if b:
        print("Success: " + testname + "; "+ msgOK)
    else:
        print("Failed: " + testname + "; "+ msgFailed)

def test_ed_replace(b, testname, msgOK="", msgFailed=""):
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)

def test_ed_append(b, testname, msgOK="", msgFailed=""):
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)

def test_ed_read(b, testname, msgOK="", msgFailed=""):
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)

def main():
    fn = "file1.txt"    # assume this file does not exist yet.
    
    try:
        ed_read(fn)
        test_ed_read(True, fn, "string appended successfully")
    except Exception as e:
        test_ed_read(False, fn, msgFailed = str(e))
    
    ed_append(fn, "0123456789")    # this will create a new file
    ed_append(fn, "0123456789")    # the file content is: 01234567890123456789
    
    print(ed_read(fn, 3, 9))    # prints 345678. Notice that the interval excludes index to (9)
    print(ed_read(fn, 3))       # prints from 3 to the end of the file: 34567890123456789
    
    lst = ed_find(fn, "345")
    print(lst)                  # prints [3, 13]
    print(ed_find(fn, "356"))   # prints []
    
    ed_replace(fn, "345", "ABCDE", 1)  # changes the file to 0123456789012ABCDE6789
    
    # assume we reset the file content to 01234567890123456789  (not shown)
    ed_replace(fn, "345", "ABCDE")  # changes the file to 012ABCDE6789012ABCDE6789
    
main()