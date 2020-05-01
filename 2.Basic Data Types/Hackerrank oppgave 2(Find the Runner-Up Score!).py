if __name__ == '__main__':
    n = int(input("Number of entries: "))
    arr = map(int, input("Scores, seperated by space").split())
        
    arr_set=set(arr)
    arr_list=list(arr_set)
    arr_sorted=sorted(arr_list, reverse=True)
    print(arr_sorted[1])

if __name__ != '__main__':    
    n = int(input())
    arr = map(int, input().split())
    print(
        sorted(
                list(
                    set(
                        arr)
                    )
                ,reverse = True)
        [1]
        )