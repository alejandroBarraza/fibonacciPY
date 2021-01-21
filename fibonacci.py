
def fib(n):
    
    if n<2:
        return n
    else:
        return (fib(n-1) + fib(n-2))
        
        
    

def main():
    
    print('Fibonacci Sequence')

    # to the first 300 numbers
    for i in range(60):
        index = i+1
        
        result = fib(i)
        print(i,":",result,"=",end=" ")
        #//calcute the factor of fibonacci sequence
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
        

    print('Finish')
    



if __name__ == "__main__":
    main()

                




