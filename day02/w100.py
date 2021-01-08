## 성별, 키, 몸무게를 입력 받는다.
## 성별 비만도를 측정한다.
## 비만인지 정상인지를 출력한다.


a = input("성별")
b = input("키")
c = input("몸무게")

d = int(b)-100;


if a == "남자" :
    if d > int(c):
        print("정상")
    if d < int(c) :
        print("비만")

