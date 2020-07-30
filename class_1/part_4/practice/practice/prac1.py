def genPrimes():
    c = 2
    while True:
        isPrime = True
        for i in range(2,c):
            if c%i == 0:
               isPrime = False
               break
        if isPrime:
            yield c
        c+=1

f = genPrimes()
next(f)
next(f)

            
