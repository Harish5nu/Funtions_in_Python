#Q> write a python program using functions to convert Fahrenheit to Celsius

def f_to_c(f):
    return 5*(f-32)/9
f=int(input("Enter Temperature in F: "))

print(F"{round(f_to_c(f),2)} °C")