import sys,math

######find the total number of divisors of a given number (whole number)



dc=0 #number of divisors


def total_of_divs(n:int):
    global dc
    if (int(math.sqrt(n))*int(math.sqrt(n)))==n:# if it's perfect square
        ps=1 #perfect square
    else:
        ps=0  #non-perfect square
        
    if ps:
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                dc+=1
        print(f"total num {dc*2-1}")
        
    else:
        print("#############not a perfect square")
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                dc+=1
        print(f"total num {dc*2}")

try:
    if sys.argv[1]:
        print(f"ur input was {sys.argv[1]}")
        total_of_divs(int(sys.argv[1].strip()))
except(Exception):
        print("User input must be an integer\n"
         "###HOW TO USE###: sys.argv[1] 25")
        


#TODO 

#option to list divisors