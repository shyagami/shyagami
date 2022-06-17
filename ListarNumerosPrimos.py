import time
start_time = time.time()

def count_primes(num):
    # check the basicaly rules of prime numbers, 0 an 1 input.
    if num < 2:
        return 0

    # 2 or greater
    # Storage the prime numbers
    primes = [2]
    # counter going up to input number
    x = 3
    # x going to every number
    while x <= num:
        # check if x is prime
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break

        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

results = count_primes(int(input('Quantos numeros primos você deseja, digite uma quantidade: ')))

print(results)
print("--- %s seconds ---" % (time.time() - start_time))
