import sys, time

print('This is the Collatz sequence problem, or the 3n+1 - problem')

print('Enter the starting number of a sequence(greater than 0) or QUIT:')
response = input('>')

if not response.isdecimal() or response == '0':
    print('Yo tengo escribo un integer > 0')
    sys.exit()

n=int(response)
print(n, end='', flush=True)
while n != 1:
        if n % 2 == 0: # if n - even
            n = n//2
        else:
            n = 3*n+1
        arr = list()
        arr += str(n)
        print(', '+ str(n), end='', flush=True)
        time.sleep(0.00000000000000000000001)

print()
