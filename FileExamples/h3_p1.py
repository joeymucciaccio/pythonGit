#Joseph Mucciaccio
#This program takes information from one file and outputs it to a second one
#also has another function that gets rid of any comments in one file and outputs it to another

def line_number(input_file, output_file):
    index = 1
    try:
        with open(input_file,'r') as inputFile:
            index = inputFile.readlines()
        
        line_number = 1
        with open(output_file,'w+') as outputFile:
            for line in index:
                outputFile.write(str(line_number) + ') ' + line)
                line_number += 1 #goes through every line
    except:
        print('Error, no file found.')



def strip_comments(source, destination, comment):
    input_file = open(source,"r")
    read = input_file.read()
    location = read.split("\n")
    new_string = ""
    for index in location:
        if (index.find(comment)!=-1):
            new_string = new_string + index[0:index.find(comment)] + "\n"
        else:
            new_string = new_string + index
  

    output_file = open(destination,"w")
    output_file.write(new_string)
    print("Comments removed.")
    

def main():
    input_file = input("Enter the file name: ")
    line_number(input_file,'test.py.txt')
    
    source = input("Enter the file name to remove comments: ")
    strip_comments(source,'test2-nocomments.txt', '#')
main()