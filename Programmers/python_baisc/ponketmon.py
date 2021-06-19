
nums=[3,1,2,3]

def solution(nums):
    #answer = 0
    list=[]
    list.append(nums[0])
    for i in range(1, len(nums)): 
        if not nums[i] in list:
            list.append(nums[i])
    
    #print(list)
    
    temp=[]
    if len(list) > len(nums)//2:
        for i in range(0, len(nums)//2):
            if not list[i] in temp:
                temp.append(list[i])
                answer=len(temp)
                if len(temp) >= len(nums)//2:
                    break
    else:
        answer=len(list)
    
    print(answer)
    return answer
solution(nums)
