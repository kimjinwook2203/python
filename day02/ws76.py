##한자리 숫자를 입력 받는다.
# 숫자의 범위는 1~9
# 아니면 프로그램 종료
# 입력 받은 숫자 까지의 합과 평균을 구하시오
a = input('숫자를 입력 하세요')
sum = 0;
avg = 0;

for n in range(int(a)) :
    sum += (n+1);
## cnt += 1; for문이 몇번 돌아갔는지 확인 하는 방법 이걸로 하기 가능
print(sum);
print(sum/(int(a)));