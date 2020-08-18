#Joseph Mucciaccio
#This program takes all possibilities of a triple sided triangle under the bound of 0 < a, b, c <= n
#and outputs them with the pythagorean theorem

def pythagorean_triple(n):
    result = []
    
    #triple nested loop to calculate the bounds for a, b, and c
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n +1):
                if a ** 2 + b ** 2 == c ** 2:
                    result.append((a, b, c))
    return result


def main():
    n = int(input("Enter a max value: "))
    
    for a, b, c in pythagorean_triple(n):
        print(a, b, c)


main()
