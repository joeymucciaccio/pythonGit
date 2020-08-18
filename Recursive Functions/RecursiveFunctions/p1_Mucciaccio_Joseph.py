#Joseph Mucciaccio
#This program contains three different functions that demostrate recursive functioning.

import turtle


def draw_leaf_straight(length, depth, branchno=1):
    
    def branch(length, depth):
        if depth == 0:
            return
        else:
            turtle.width(depth)
            turtle.forward(length)
            branch(length/2, depth-1)
            turtle.backward(length*1/3)
            turtle.left(60)
            branch(length/3, depth-1)
            turtle.right(120)
            branch(length/3, depth-1)
            turtle.left(60)
            turtle.backward(length*2/3)
    
    if branchno > 0:
        branch(length, depth)
        turtle.left(90)
        
        draw_leaf_straight(length, depth, branchno - 1)

turtle.left(90)
turtle.delay(0)
draw_leaf_straight(120, 6)

print("b)")

#b) base x conversion
def strB(n, base = 10):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    digits.extend(['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])
    digits.extend(['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    if n == 0:return str('')
    else:
        remainder = n % base
        n = n // base
        return str(strB(n, base)) + str(digits[remainder])


def testif(b,testname,msgOk='',msgFailed=''):
    if b:
        print('Success: '+testname+": "+msgOk)
    else:
        print('Failed: ' + testname + ": " + msgFailed)
    return b

convert1 = strB(1234, base = 10)
testif(convert1 == '1234','Test 1','Base 10 Working','Base 10 Not Working')
convert2 = strB(10, base = 8)
testif(convert2 == '12','Test 2','Base 8 Working','Base 8 Not Working')
convert3 = strB(15, base = 25)
testif(convert3 == 'F','Test 3','Base 25 Working','Base 25 Not Working')
convert4 = strB(123456789, base = 26)
testif(convert4 == 'AA44A1','Test 4','Base 26 Working','Base 26 Not Working')


#c) Memoized binomial coefficient
def Cnk_m(n, k):
    array = [0 for i in range(k + 1)]
    array[0] = 1
    for i in range (1, n + 1):
        j = min(i, k)
        while (j > 0):
            array[j] = array[j] + array[j - 1]
            j = j - 1
    return array[k]


print("--------------------------------------")
print("c)")

test1 = Cnk_m(9, 4)
testif(test1 == 126,'Test 1','9 choose 4 Working','9 choose 4 Not Working')
test2 = Cnk_m(10, 2)
testif(test2 == 45,'Test 2','10 choose 2 Working','10 choose 2 Not Working')
test3 = Cnk_m(8, 7)
testif(test3 == 8,'Test 3','8 choose 7 Working','8 choose 7 Not Working')
test4 = Cnk_m(20, 10)
testif(test4 == 184756,'Test 4','20 choose 10 Working','20 choose 10 Not Working')


