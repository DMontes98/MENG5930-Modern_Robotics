Temp = float(input('Input the temperature (deg C): '))
print('Temp = ',Temp)
if(Temp < -30 or Temp > 200):
    print('Extreme temperature')

if (Temp < 0):
    print('Water is ice')
elif(Temp < 80):
    print('Water is liquid')
elif(Temp < 100):
    print('Water is super hot liquid')
else:
    print('water is gas')

print('Science for today')

# Boolean variables
warm = (Temp > 30)
print('warm = ', warm)
if (warm):
    print('short sleeve today')
else:
    print('Wear a coat')
