import math
def main():
    print('Welcome to the vector conversion calculator!')
    print('---------------------------------------------')
    for i in range(2):
        X = float(input('Enter x component of vector: '))
        Y = float(input('Enter y component of vector: '))
        Conjugate(Y)
        print('The conjugate of vector',(X,Y),'=',(X,Conjugate(Y)))
        Polar(X,Y)
        print('The polar coordinates of vector',(X,Y),'=',Polar(X,Y))

def Conjugate(Y):
    Y = Y*-1
    return(Y)

def Polar(X,Y):
    Radius = math.sqrt(X**2 + Y**2)
    Theta = math.degrees(math.atan(Y/X))
    return(Radius,Theta)

main()
