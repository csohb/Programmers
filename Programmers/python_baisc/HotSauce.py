scoville=[1, 3, 2, 9, 10, 12]
K=7

def solution(scoville, K):
    answer = 0
    '''
        1.
            가장 작은 지수 min으로 찾음
            1-1 가장 작은 지수 k보다 크면 return answer
            1-2 for문으로 그 다음 작은 지수 찾음
                배열에서 두개 제거
                새로운 음식 스코빌지수 계산
                answer+=1
                새로운 음식 배열에 추가
    '''
    
    # 가장 작은 음식이 K보다 클때
   
    while min(scoville) < K:
        scoville.sort()
        try:
            scoville.append(scoville.pop(0)+(scoville.pop(0)*2))
        except IndexError:
            return -1
        answer+=1
    
    print(answer)
    return answer
solution(scoville, K)