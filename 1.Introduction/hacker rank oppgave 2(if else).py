n = 0

print("Write a number between 1 and 100:")

n = int(input())

while 1 < n <= 100:

    if (n % 2) != 0:
        print("Weird")

    elif (n % 2) == 0 and 1<n<=5:
        print("Not Weird")

    elif (n % 2) == 0 and 5<n<=20:
        print("Weird")

    elif(n % 2) == 0 and n>20:
        print("Not Weird")
        
    print("Write a number between 1 and 100:")
    n = int(input())
    
    


    
