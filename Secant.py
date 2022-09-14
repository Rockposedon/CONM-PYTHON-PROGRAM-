# Defining Function
def f(x):
    return x ** 3 - 5 * x - 9


# Implementing Secant Method

def secant(a, b, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(a) == f(b):
            print('Divide by zero error!')
            break

        m = a - (b - a) * f(a) / (f(b) - f(a))
        print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))
        a = b
        b = m
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(f(m)) > e
    print('\n Required root is: %0.8f' % m)


# Input Section
a = input('Enter First Guess: ')
b = input('Enter Second Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
a = float(a)
b = float(b)
e = float(e)

# Converting N to integer
N = int(N)

# Starting Secant Method
secant(a, b, e, N)

