#3

try:
    k = 5//0 # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
# this block is always executed
# regardless of exception generat
    print('This is always executed')
