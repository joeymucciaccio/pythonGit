#Joseph Mucciaccio
#This program consists of a variety of list comprehension examples

#a
print("a)")
print([i * i for i in range(0,26)])
print("-" * 48)

#b
print("b)")
print([str(i)+"**2 = " + str(i**2) for i in range(0,26)])
print("-" * 48)

#c
print("c)")
print([(a,b,c) for a in range(1, 100 + 1) for b in range(1, 100 + 1) for c in range(1 , 100 + 1)  if a**2 == b**2 + c**2 ])
print("-" * 48)

#d
print("d)")
number_list = ['one','seven','three','two','ten']
print([(len(i),i.upper()) for i in number_list if len(i) > 3])
print("-" * 48)

#e
print("e)")
names_list = ['Jules Verne','Alexandre Dumas','Maurice Druon']
print([i[i.index(' ') + 1:]+', ' + i[0:i.index(' ')] for i in names_list])
print("-" * 48)

#f
print("f)")
def unzip(seq):
    first, second = [], []
    for i in seq:
        first.append(i[0])
        second.append(i[1])
    return tuple([first,second])

lst = [(1, "one"),(2, "two"),(3, "three")]
tup = unzip(lst)  
print(tup)
print("-" * 48)

#g
print("g)")
def concatenate(seperator,*argument):
    if len(argument) == 1:
        return argument[0]
    else:
        start = argument[0]
        for i in range(1, len(argument)):
            start += seperator + argument[i]
    return start

print(concatenate(':',"one","two","three"))
print(concatenate(' and ',"Bonny","Clyde"))
print(concatenate('and',"single"))
print("-" * 48)

#h
print("h)")
lst = list(range(0,20))
print(lst[16 : 10 : -1])
print("-" * 48)

#i
print("i)")
lst = list(range(0,20))
print(lst[16 : 10 : -2])
print("-" * 48)