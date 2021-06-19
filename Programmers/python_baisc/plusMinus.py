absolutes=[4,7,12]
signs=[True,False,True]
def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        if signs[i] == True:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    print(answer)
    return answer

solution(absolutes, signs)