import pdb


pdb.set_trace()

# list of num lists
listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
listas_numeros = [3, 4, 8, 5, 5, 22, 13]


def getMaxNumbers(numLists: list) -> list:
    result = [max(listNums) for listNums in numLists]
    return result


def getPrimeNumbers(num:int) -> bool:
    if num % 2 != 0:
        return True
    return False


# get max number for each list
maxnumoflists = getMaxNumbers(listas)
print(maxnumoflists)

# get prime numbers
prime_numbers = filter(getPrimeNumbers, listas_numeros)
print(list(prime_numbers))