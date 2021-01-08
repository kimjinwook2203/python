## 진위형 트루 펄스
temp = None; ## 이거는 변수 선언인데 정수 실수 어떤걸
            ## 넣을지 몰라서 하는거임

a = True;
b = (10>20);
print(a);
print(b);
print (a or b);

data = [1,2,3,True,"5"]; ## 여러개의 데이터 list라고 부름 얘는 변경 가능
            #보통 array 라고 부르는데 파이썬에선 list라고 부름
print (data)
print (data[2]);
print (len(data));
print ("----------------")
for n in range(5) :
    print ("값",data[n]);

print ("----------------")
for n in data :
    print(n);

print ("----------------")

data2 = (2,3,4,5,6); ## tuple 이건 변경을 할 수 없음 한번 이렇게 만들어 놓으면 끝가지 이 값을 갖는다
for n in data2 :
    print(n);