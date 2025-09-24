#Q> write a python function to print multiplication table fo given number.

def mult(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

mult(5)