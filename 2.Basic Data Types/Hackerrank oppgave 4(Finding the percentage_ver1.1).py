import random
# N students 
#contains name and prosent score in 3 subjects 

# N = int(input())

students = {}

print(students)

new_students = {"alex":[52,12,5], "Thomas":[40,20,10], "Anders":[15,20,30]}


students.update(new_students)

    
print(students)

for x in students:
    print(x)






# =============================================================================
# hvordan regne ut gjennomsnittet i en liste:
# =============================================================================

def gjennomsnittet():
    my_list = []
    x = int(input("How many numbers to the list? "))
    for n in range(x):
        numbers = random.randint(0, 25)
        my_list.append(numbers)
        
    print(my_list)
    
    print("Summen er: ", sum(my_list))
    
    my_avg = sum(my_list) / x 
    print("Gjennomsnitt er:",my_avg)
    
    #evt 
    
    print("Gjennomsnitt er også",sum(my_list) / x)
#gjennomsnittet()