
my_list = []
print("how big's the list: ")   

for i in range(int(input())):
    

    
    print("name for index", i, ": ")
    name = input()
    
    print("Whats the grade: ")
    score = float(input())
    my_list.append([name, score])
    
    grades = [g[1] for g in my_list]
    grades.sort(reverse=True)
    
    first = float("inf")
    second = float("inf")
    
    for grades in grades :
        if grades < first :
            second = first 
            first = grades
noob_list = [ x[0] for x in my_list if x[1] == second ]
noob_list.sort()


print("second lowest score is: ", *noob_list, sep="\n")
print(my_list)
            
#second_lowest = my_list.index(second)
    
#print(second_lowest)        
    
#print(second)    
#print("List is: ", my_list) 
#print(grades)
#print("2nd lowes is: ", grades[1])
#print(first)


