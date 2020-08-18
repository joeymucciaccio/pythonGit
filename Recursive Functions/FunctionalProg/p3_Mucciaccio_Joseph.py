#Joseph Mucciaccio
#This program demostrates the use of functional programming by creating an infinite sequence of tuples and putting them through tests

from itertools import islice, filterfalse
from functools import reduce

# PART A
def rnd_gen(x0, n):
    m = 2**32
    a = 22695477
    c = 1
    if n > 0:
        for i in range(n + 1):
            x1 = (x0 * a + c) % m
            x0 = x1
            n += 1
            yield x1
    else:
        while True:
            x1 = (x0 * a + c) % m
            x0 = x1
            n += 1
            yield x1
  
def gen_rndtup(m):
    rnd = rnd_gen(1, -1)
    while True:
        a = next(rnd) % m
        b = next(rnd) % m
        yield (a, b)

def main():

    #a)
    gen = gen_rndtup(50)
    print("------------------------")
    print("a)")

    print("no islice")
    count = 10
    r_count = 0
    for tupl in gen:
        print('{:>3}: {}'.format(r_count + 1, next(gen)))
        r_count += 1
        if r_count == count:
            break

    gen = gen_rndtup(50)
    print("------------------------")
    print("islice")
    first_10 = islice(gen, 0, 10)
    count = 0
    for tupl in first_10:
        count = count + 1
        print('{:>3}: {}'.format(count, tupl))

    #b)
    print("------------------------")
    print("b)")
    gen2 = gen_rndtup(10)
    
    def less_eq_six(tupl): return tupl[0] + tupl[1] <= 6
    
    filtered_list = filterfalse(lambda y: less_eq_six(y) == False, gen2)
    first_8 = islice(filtered_list, 8)
    
    count = 1
    for tupl in first_8:
        print('{:>3}: {}'.format(count, tupl))
        count = count + 1

    #c)

    print("------------------------")
    print("c)")

    a_it = (a % 100 for a in rnd_gen(1, -1))
    b_it = (b % 100 for b in rnd_gen(2, -1))
    
    a_list = []
    b_list = []
    
    count = 0
    while count < 8:
        for a in a_it:
            for b in b_it:
                if a <= b:
                    a_list.append(a)
                    b_list.append(b)
                    count = count + 1
                    break
            if count >= 8:
                break

    zipd = zip(a_list, b_list)
    index = 1
    for tupl in zipd:
        print('{:>3}: {}'.format(index, tupl))
        index = index + 1

    #d)
    print("------------------------")
    print("d)")
    values = rnd_gen(1, -1)
    modified = islice(filter(lambda x: x %
                             13 == 0, map(lambda y: y % 100, values)), 10)

    index = 1
    for value in modified:
        print('{:>3}: {:3}'.format(index, value))
        index += 1

    mapped = map(lambda y: y % 100, values)
    filtered = filter(lambda x: x % 13 == 0, mapped)
    isliced = islice(filtered, 10)
    for value in isliced:
        pass
    
    #e)
    print("------------------------")
    print("e)")
    test1 = gen_rndtup(10)
    test1_s = islice(filter(lambda z: z[0] + z[1] >= 5, test1), 10)
    test1_s_x = map(lambda x: x[0], test1_s)
    test1_s = islice(filter(lambda z: z[0] + z[1] >= 5, test1), 10)
    test1_s_y = map(lambda x: x[1], test1_s)

    x_list = []
    y_list = []
    x_list_int = []
    y_list_int = []

    for ind in test1_s_x:
        x_list.append(str(ind))
        x_list_int.append(ind)
    x_list = "+".join(x_list)

    for ind in test1_s_y:
        y_list.append(str(ind))
        y_list_int.append(ind)
    y_list = "+".join(y_list)

    reduceX = reduce(lambda x,y: x + y, x_list_int)
    reduceY = reduce(lambda x,y: x + y, y_list_int)

    print("Sum of ({}, {}) = ({}, {})".format(x_list, y_list, reduceX, reduceY))


if __name__ == "__main__":
    main()