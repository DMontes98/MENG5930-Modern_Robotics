import random
def main():
    Yuh = [0,0,0,0,0,0,0,0,0,0,0,0,0] # representing the array that the 13 different types will be thrown into
    Integers = 4*52 # Number of cards calculating to 208
    for h in range(Integers):
        Tonka = random.randint(1,13)
        for b in range(1, 14):
            if (Tonka == b):
                Yuh[b-1] += 1
    for c in range(1,14):
        print('Number of ',c,' cards = ',Yuh[c-1])
    print(CalculateMax(Yuh),' had the most cards dealt')
            
def CalculateMax(Yuh):
    Variable = max(Yuh)
    NewVariable = Yuh.index(Variable) + 1
    return (NewVariable)


main()
