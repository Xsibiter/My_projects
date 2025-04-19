'''Program that shows different '''


while True:
    response = input('Enter the starting number: ')
    if response == '':
        response = '0'
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display: ')
    if response == '':
        response = '100'
        break
    if response.isdecimal():
        break
    print('Please, enter a number')
amount = int(response)

for num in range(start, start+amount):
    hexNumber = hex(num)[2:].upper()
    binNumber = bin(num)[2:]
    octNumber = oct(num)

    print('DEC:', num, ' HEX:', hexNumber, ' BIN:', binNumber, 'OCT:', octNumber)