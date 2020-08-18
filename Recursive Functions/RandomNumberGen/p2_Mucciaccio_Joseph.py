#Joseph Mucciaccio
#This program generates a sequence of pseudo-random numbers with the use of a linear congruential generator (LCG).



class RndSeq():

    m = 2**32
    a = 22695477
    c = 1

    def __init__(self, x0, n):
        self.__x0 = x0
        self.__n = n
        self.__count = 1



    def __iter__(self):
        return self

    def __next__(self):
        if self.__count>self.__n:
            raise StopIteration
        else:
            self.__x0 = (RndSeq.a * self.__x0 + RndSeq.c) % RndSeq.m
            self.__count += 1
            return self.__x0

rnd = RndSeq(1,10)
print([i for i in rnd])



#b)
def rnd_gen(x0,n):
    m = 2**32
    a = 22695477
    c = 1
    while n > 0:
        x0 = (a * x0 + c) % m
        yield x0
        n -= 1

print([i for i in rnd_gen(1, 3)])