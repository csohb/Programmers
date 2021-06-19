import re

arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
n=5

# 2진법 변환 함수
def toBinary(arr, n):
    for i in range(0, n):
        arr[i]=format(arr[i], 'b')
        if len(arr[i]) < n:
            arr[i]=arr[i].zfill(n)
    return arr

def solution(n, arr1, arr2):
    answer = ['#'*n]*n
    
    print(answer)
    
    arr1=toBinary(arr1, n)
    arr2=toBinary(arr2, n)
    print(arr1)
    print(arr2)
    
    
    for i in range(0, n):    
        for j in range(0, n):
            if arr1[i][j]=='0' and arr2[i][j]=='0':
                answer[i][j].replace('#', ' ')
            
        
    print(answer)        
    
    
    
    return answer

solution(n, arr1, arr2)
