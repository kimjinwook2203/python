score = [90,80,60,100];
#score.sort(); # 스코어의 변수의 메모리는 그대로 두고
            # 메모리 구조 그대로에서 순서만 바꾼거
            #거꾸로는    score.sort(reverse=True);
score2 = sorted(score);#새로운 list만들기
#거꾸로 score2 = sorted(score,reverse=True);
print(score);
print(score2);

for i in enumerate(score2,1):#1번부터 시작해라
    print(i,sep=' ');#tuple로 나옴