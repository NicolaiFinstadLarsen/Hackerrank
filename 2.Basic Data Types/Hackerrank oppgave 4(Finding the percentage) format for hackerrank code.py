from decimal import Decimal
#if __name__ == '__main__':
    
    
#        n = int(input())
#    student_marks = {}
#    for _ in range(n):
#        name, *line = input().split()
#        scores = list(map(float, line))
#        student_marks[name] = scores
#    query_name = input()
    
    
    
    total = float((sum(student_marks[query_name])))
    avg = total / len(student_marks[query_name])
    avg_dec = Decimal(avg)
    print(round(avg_dec,2))

