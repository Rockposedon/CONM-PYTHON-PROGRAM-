# FALSE POSITION METHOD TO FIND THE ROOT OF NON LINAER QUADRATIC EQUATION

def f(x):
    return x**3-5*x-9

def FALSE(a,b,e):
    step = 1
    print('\n\n *regula false method calculation*')
    condition = True
    while condition:
        m = a - (b-a) * f(a) /( f(b) - f(a) )
        print('iteration-%d, m = %0.6f and f(m) = %0.6f' % (step, m, f(m)))

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

            step = step + 1
            condition = abs(f(m)) > e

            print('\nRequired root is : %0.8f' % m)

a = input('First Guess: ')
b = input('Second Guess: ')
e = input('Tolerable Error: ')

a = float(a)
b = float(b)
e = float(e)

'''            a = flaot(input('first guess:'))
            b = flaot(input('second guess:'))
            e = flaot(input('tolerable error:'))
'''
if f(a) * f(b) > 0.0:
    print('not the right point.')
    print('wrong guess.')
else:
    FALSE(a,b,e)
