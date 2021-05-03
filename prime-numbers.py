check_prime = []
x = True

while x:
    user_prime = int(input("Please enter a number. '0' to end. "))
    if user_prime == 0:
        x = False
        break
    else:
        check_prime.append(user_prime)

for prime in check_prime:
    factor_count = 0

    for i in range(2, prime):
        if prime % i == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(prime, i, prime))
            factor_count += 1

    if factor_count > 0:
        print("{} has {} factors".format(prime, factor_count))

    if factor_count == 0:
        print("{} is a prime number".format(prime))
