## 4개의 성적 입력 받는다, 4개의 평균을 구한다
## 90이상 a, 80~90 b 70~80c 60~70d 60미만 f
print("start");
ko = input("ko 점수");
en = input("en 점수");
si = input("si 점수");
ma = input("ma 점수");

sum = int(ko) + int(en) + int(si) + int(ma);
avg = int(sum)/4

print(avg)

if avg > 90 :
    print("A")
elif avg >= 80 :
    print("b")
elif avg >= 70 :
    print("c")
elif avg >= 60 :
    print("d")
else :
    print("F")

print("end");