# Try-except 
def divide_numbers(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Division by zero error"
    except:
        return "Invalid"

# here we also handled the invalid input error as well. so depending on the situation we can handle the error

print(divide_numbers(5,2))
print(divide_numbers(5,0))
