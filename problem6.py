#Q> write a python function which converts inches to cms.
i=int(input("Enter number is inches: "))
def inch_to_cm(i):
    return i*2.54
print(f"The corresponding value is :{inch_to_cm(i)} cm")