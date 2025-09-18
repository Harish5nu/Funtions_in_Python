#Q> write a program using functions to find grestest of three numbers.

a=1 
b=24
c=3 
def grestest (a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
print(grestest(a,b,c))
        