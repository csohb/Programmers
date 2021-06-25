user_input = int(input())
count=0
for i in range(1, user_input):
    if i <= 10 and i%3==0:
        count+=1
        print(i)
    elif i > 10 and i <= 100:
        if (i//10)%3 == 0: 
            count+=1
            print(i)
        if (i%10)%3 == 0:
            
            if i%10==0:
                continue
                print(i)
            else:
                count+=1
                print(i)
print(count)