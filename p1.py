nterms = int(input("How many terms? "))

# first two terms
#n1 = 0
#n2 = 1
#count = 2

def fib(n):
    if n <= 0:
       print("Plese enter a positive integer")
       return 0;
    elif n == 1:
       #print("Fibonacci sequence:")
       return 0;
    elif n == 2:
        return 1;
    else:
        return fib(n-1) + fib(n-2);
print (fib(nterms));
