#SERGIO ESTUARDO RUANO NAJARRO 
#201612203




def collatz(num):
    while(num != 1):
        if(num %2> 0):
            num = 3*num +1
            yield num
        else:
            num = num/2
            yield num

            

n=203
for i in range(2,n):
    print(list(collatz(i)))
  


