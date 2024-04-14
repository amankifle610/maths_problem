import random
import time
sign = ['+','-','*']
input("Please enter to start")
start=time.time()
for i in range(10):
    s=random.randint(0,2)
    num1=random.randint(0,51)
    num2=random.randint(0,51)
    if(s==0):
        print("Problem "+str(i+1)+": "+str(num1)+" + "+str(num2)+" =",end =" ")
        a=int(input())
        answer=num1+num2
        while (a==answer)==False:
            print("     please try again!!")
            print("     "+str(num1)+" + "+str(num2)+" =",end =" ")
            a=int(input())
            
    elif(s==1):
        print("Problem "+str(i+1)+": "+str(num1)+" - "+str(num2)+" =",end =" ")
        a=int(input())
        answer=num1-num2
        while a!=answer:
            print("     please try again!!")
            print("     "+str(num1)+" - "+str(num2)+" =",end =" ")
            a=int(input())
    else:
        print("Problem "+str(i+1)+": "+str(num1)+" * "+str(num2)+" =",end =" ")
        a=int(input())
        answer=num1*num2
        while a!=answer:
            print("     please try again!!")
            print("     "+str(num1)+" * "+str(num2)+" =",end =" ")
            a=int(input())
end=time.time()
print("Nice work! you finished in "+str(round(end-start,2))+" seconds.")
