# BISECTION METHOD TO FIND THE ROOTS OF NON LINEAR EQUATION(PYTHON PROGRAM)

def f(x):
    return x ** 3 - 5 * x - 9


def bisection(a, b, e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        m = (a + b) / 2
        print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))

        if f(a) * f(m) < 0:
            b = m
        else:
           a = m

        step = step + 1
        condition = abs(f(m)) > e

    print('\nRequired Root is : %0.8f' % m)


a = input('First Guess: ')
b = input('Second Guess: ')
e = input('Tolerable Error: ')

# Converting input to float
a = float(a)
b = float(b)
e = float(e)



if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a, b, e)
