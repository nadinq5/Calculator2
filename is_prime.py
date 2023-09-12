def is_prime(result):
    counter = 1
    range_length = result//2 + 1


    for i in range(range_length):
        if result % (i + 1) == 0:
            counter += 1

    if counter > 2:
        print(f'{result} is not a prime number.')
    else:
        print(f'{result} is a prime number.')