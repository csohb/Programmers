numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
def solution(numbers, hand):
    '''
        풀이법 생각
        1,4,7 => 무조건 왼손
        3,6,9 => 무조건 오른손
        2,5,8,0=>두 엄지 손가락의 현재 키패드 위치에서 더 가까운 엄지손가락 사용
        거리가 같으면 어느 손잡이인지에 따라 다름
        
        왼손 오른손 현재위치 계속 기억해야함
        -> for문 돌려서?
        
    '''
    answer = ''
    # 왼손 오른손 현재위치 저장하는 변수 
    left=10
    right=12
    for i in range(0, len(numbers)):
            if numbers[i]==0:
                numbers[i]=11
            if numbers[i]==1 or numbers[i]==4 or numbers[i]==7:
                answer+='L'
                left=numbers[i]
            elif numbers[i]==3 or numbers[i]==6 or numbers[i]==9:
                answer+='R'
                right=numbers[i]
            else:
                numbers[i] = 11 if numbers[i] == 0 else numbers[i]
                absL=abs(numbers[i]-left)
                absR=abs(numbers[i]-right)
                
                if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                    answer+='R'
                    right=numbers[i]
                elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                    answer+='L'
                    left=numbers[i]
                else:
                    if hand == 'left':
                        answer+='L'
                        left=numbers[i]
                    else:
                        answer+='R'
                        right=numbers[i]
                    
                    
                    
                

    print(f"answer={answer}")        
    return answer

solution(numbers, hand)