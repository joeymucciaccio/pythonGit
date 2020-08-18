#Joseph Mucciaccio
#This program consists of a list of task to complete for 4-dimension vectors


class NVector(object):
    
    # a) constructor
    def __init__(self, *values):
        if(len(values) == 1):
           # raises error if it is not a sequence
           if(not isinstance(values[0], (list, tuple))):
               raise TypeError
           # assigns sequnce to vector
           else:
               self.vector = list(values[0][:])
       # assigns arbitrary length values to vector
        else:
           self.vector = list(values[:])
     
    # b) length of vector    
    def __len__(self):
        return len(self.vector)
    
    # c) index operator
    def __getitem__(self, index):
        return self.vector[index]
    
    # d) indexed assignment operator
    def __setitem__(self, index, data):
            self.vector[index] = data
            
    # e) string representation
    def __str__(self):
        return str(self.vector)
    
    # f) equal to parameter
    def __eq__(self, other): #equal
        return self.vector == other
    def __ne__(self, other): #not equal
        return self.vector != other
    
    # g) addition between vectors
    def __add__(self, other):
        if isinstance(other, NVector):
            l = min(len(other), len(self.vector))
            temp = []
            for i in range(l):
               temp.append(other[i] + self.vector[i])

            for i in range(max(len(other), len(self.vector)) - l):
               temp.append(other[i] if(len(other) > l) else self.vector[i])

            return NVector(temp)

       # adds scalar to the vector
        else:
           return NVector([i+other for i in self.vector])
    
    def __radd__(self, other):
       return NVector([i+other for i in self.vector])
    
    # h) multiplication between vectors
    def __mul__(self, other):
         if(isinstance(other, NVector)):
           # if both are of not same length, return error
           if(len(other) != len(self.vector)):
               return TypeError
           value = 0

           # performs dot product
           for i in range(len(other)):
               value += other[i] * self.vector[i]

           return value
         else:
           return NVector([i*other for i in self.vector])

    def __rmul__(self, v):
       return NVector([i*v for i in self.vector])
    
    # i) zero for all elements
    def zeros(self, n):
        return NVector([0]*n)
    
    def testif(b, testname, msgOK="", msgFailed=""):
        if b:        
            print("Success: "+ testname + "; " + msgOK)    
        else:
            print("Failed: "+ testname + "; " + msgFailed)    
        return b
    # MAIN
    def __main__(testif):
        testif(NVector([1,2,3, 4]) == NVector(1, 2, 3, 4), 'constructor works', "constructor failed")
        test = NVector(1, 2, 3, 4)

        # tests setitem, getitem
        test[1] = 8
        testif(test[1] == 8 , msgOK="setitem works", msgFailed="setitem failed")
    
    
        # test len
        testif(len(test) == 4, "len works", "len failed")
    
        # eq test
        testif(test == test, "eq works", "eq failed")
    
        #nq test
        testif(not(test != test), "nq works", "nq failed")
    
        # add test
        testif(test + test1 == NVector([2, 16, 6, 8]), "add works", "add failed")
        testif(test + 2 == NVector([3, 10, 5, 6]), "add with scalar works", "add with scalar fails")
        testif(2 + test == NVector([3, 10, 5, 6]), "radd works", "radd failed")
    
        # mul, rmul
        testif(test * test1 == 90, "Mul with vector works", "mul with vector fails")
        testif(test * 3 == NVector([4, 32, 12, 16]) , "Mul with scalar works", "mul with scalar fails")
        testif(3 * test == NVector([4, 32, 12, 16]), " rmul works", "rmul fails")
    
        testif(test.zeros(4) == NVector([0, 0, 0, 0]), "zeros works", "zeros fails")
    
print(NVector([1, 2, 3, 4]))
print(NVector((1, 2, 3, 4)))
print(NVector(1, 2, 3, 4))
        
print("\nvector testing:")
test = NVector(1, 2, 3, 4)
test1 = NVector([1, 8, 3, 4])
test2 = NVector([1, 2, 3, 4])
test[1] = 8
print(test)
print(test1)
print(test2)
print("len, index 1")
print(len(test), test[1])
        
print("\nequal:")
print(test == test1, test == test2)

print("\nnot equal:")
print(test != test1, test != test2)
    
print("\naddition:")
print(test + test1)
print(test + 2)
    
print("\nr-addition:")
print(2 + test)

print("\nmultiplication (*4):")
print(test * test1)
print(test * 4)
    
print("\nrmultiplicaton (*4):")
print(4 * test)
    
print("\nzeros:")
print(test.zeros(4))