## for 문 2번 돌리는 예제
## 짝수 단만 찍으시오
for n in range (2,10) :
    if n % 2 ==1 :
        continue;

    print(str(n)+"단");
    for d in range(1,10):
        print(n,d,(n*d),sep="-");
