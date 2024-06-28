'''

Name exception
Zero exception
value exception
index exception
key exception
file exception

'''
try:
    a = int(input("Enter the a values"))
    b = int(input("Enter the a values"))
    #c = a/b
    print("value of c:",a/b)
    x = [1,2,3,4]
    print(x[5])


except NameError:
    print(" b value is not mentioned")
except ZeroDivisionError:
    print("Arithematic exception")
except ValueError:
    print("Value error")
except IndexError:
    print("Array index out of bounds")
except KeyError:
    print("Key error")
except IOError:
    print("file input or output error")

print("After exception")