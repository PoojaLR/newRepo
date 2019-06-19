N=2


def fib(n,N,p1,p2):
      if n==1:
            if N==1:
                return 0;
            elif N==2:
               return 1;
            else:
               p1=1;
               p2=0;
               
      if n<N:         
         return fib(n+1,N,p1+p2,p1);
      else:
         return p1;
      


while N != 0:
   N = int(input("How many terms? "));
   print (fib(1,N,0,0));
