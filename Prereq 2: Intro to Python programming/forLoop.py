print('Number 1:')
nput = -1

while (nput < 0 or nput > 25000000):
    nput = int(input('Enter an integer: '))

variable2 = 0
for q in range(2, nput):
    if (nput % q == 0):
        variable = q
        variable2 = 5
        
if (variable2 == 5):
    print('{0} is not prime'.format(nput))
    print('The largest factor is ', variable)
else:
    print('{0} is prime'.format(nput))
