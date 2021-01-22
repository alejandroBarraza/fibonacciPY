import multiprocessing
import multiprocessing as mp

#function for calculate fibannaci number
def fib(n):

    if n<2:
        return n
    else:
        return (fib(n-1) + fib(n-2))

#calcute the factor of fibonacci sequence
def fac(result):
    
    divide=2
    if result<6:
        print(result)
    else:
        while result !=1:
            if result % divide == 0:
                print(divide,end=" ")
                result = result/divide
                if result !=1:
                    print("x ",end=" ")
                        
            else:
                divide+=1
            
    print("")
    

#main class        
def main():
    
    print('Fibonacci Sequence')
    # paralleing throught pool.
    p = multiprocessing.Pool(mp.cpu_count())
    n=0

    #the first 300 fibonacci numbers
    while(n<300):
        number = p.map(fib,[n]) 
        #result = fib(i)
        print("fibo",n,":", number , "=",end=" ")
        fac(number[0])
        n+=1      
    print('Finish')
    
#calling main class    
if __name__ == "__main__":
    
    main()

                




