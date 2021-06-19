import itertools
from pickle import FALSE, TRUE
nums=[1,2,3,4]
def solution(nums):
    answer = 0

    '''
        for문을 몇번 돌릴지 
        len(nums)
        세개 뽑아서 더해서 소수가 나오면 answer에 +1을 해줌
        1. 중복없이 3개를 랜덤으로 배열로 만들기
        2. 더해서 소수가 나오는지
        소수인지 구하는 법 
        - 1과 자기 자신만으로 나누어 떨어질때
            나머지 수로 나누면 나눠 떨어지지 않음
            
    '''
    nums2=list(itertools.combinations(nums,3))
    print(nums2)
    sumList=[]
    
    for i in range(0, len(nums2)):
        sum=0
        for j in range(0, 3):
            sum+=nums2[i][j]
        sumList.append(sum)
    print(sumList)
    
    
    
    for i in sumList:
        sosu=[]
        for j in range(2, i):
            print(f"i={i},j={j}")
            if i%j == 0: 
                sosu.append(1)
                break
        print(sosu)
        if len(sosu) == 0:
            answer+=1
            
    
    print(answer)
    return answer

solution(nums)