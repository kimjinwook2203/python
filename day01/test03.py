# 숫자를 입력 받는다.
# 1에서 입력 받은 숫자 만큼 출력 한다.
# 합과 평균을 최정 적으로 출력 하시오
a = (input('숫자를 입력 하세요'))
sum = 0;
avg = 0;
for y in range(1,int(a)+1) :
    sum += y;
    avg = (int(sum)/int(a))
    print (y)


print(sum);
print(avg);