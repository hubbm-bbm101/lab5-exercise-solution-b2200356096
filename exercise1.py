N = int(input("Please enter a number:"))

def sum_odd (N):

    sum = 0
    for i in range(N + 1):
        if (i % 2 != 0):
            sum += i
    return sum

def average_even (N):

    count = 0
    multi = 0
    for i in range(1,N + 1):
        if (i % 2 == 0):
            count += 1
            multi += i
    average = multi / count
    return average

print(sum_odd(N),average_even(N))

