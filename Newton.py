# defining function
# m = mid pont and b = any point in line
def f(x):
    return x ** 3 - 5 * x - 9


# defining derivative of function
def g(x):
    return 3 * x ** 2 - 5


# Implementing Newton Raphson Method

def newtonRaphson(b, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(b) == 0.0:
            print('Divide by zero error!')
            break

        m = b - f(b) / g(b)
        print('Iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))
        b = m
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(m)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % m)
    else:
        print('\nNot Convergent.')

b = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

b = float(b)
e = float(e)

N = int(N)
newtonRaphson(b, e, N)