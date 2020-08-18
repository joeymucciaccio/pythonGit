#Joseph Mucciaccio
#This program takes a string of letters and returns a new string that has no vowels, it also find duplicates 

def no_vowels(string):
    
    no_vowels_string = ""
    vowels = ['a','e','i','o','u']
    
    for char in string:
        if char in vowels:
            continue
        
        no_vowels_string += char
    
    return no_vowels_string

def find_dup(s, n):
    length = len(s)
    sub_s = slice(n)
    duplicates = s[sub_s]
    sub_s = slice(1, length)
    s = s[sub_s]
    
    while(length > 0):
        if(s.find(duplicates) != -1):
            return duplicates
        if(length < n or s.find(duplicates) == 0):
            return ""
        

    
def main():
    print(no_vowels('Python rules!'))
    print(no_vowels('Joey'))
    print(find_dup('abcdefgabcgh', 3))
    print(find_dup('ABCDEG', 1))
    
    #Attempted to get user input
    #string = (input("Enter a string: "))
    #no_vowels(string)

main()