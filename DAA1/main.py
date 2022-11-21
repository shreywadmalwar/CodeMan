#Nth 

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#FIRST N 

def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
    # printing fibonacci numbers
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
n = 7
for i in range(0, n):
    print(fibonacci_numbers(i), end=" ")


#First N iterative 
def printFibonacciNumbers(n):           #STEP COUNTS
    f1 = 0                              #1
    f2 = 1                              #1
    if (n < 1):                         #1
        return                          #1
    print(f1, end=" ")                  #1
    for x in range(1, n):               #n
        print(f2, end=" ")              #1
        next = f1 + f2                  #1
        f1 = f2                         #1
        f2 = next                       #1