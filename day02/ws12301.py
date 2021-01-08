# 위 데이터의 합과 평균을 구하시오
# A~F 학점을 출력하시오
# 제출은 ws1230김진욱 두개를 한꺼번에 제출

data = [98,87,90,34,56,43];
sum = data[1]+data[2]+data[3]+data[4]+data[5]+data[0]
print("합:",sum);
avg = int(sum)/6
print("평균:",avg)

if avg > 90 :
    print("학점:","A")
elif avg >= 80 :
    print("학점:","b")
elif avg >= 70 :
    print("학점:","c")
elif avg >= 60 :
    print("학점:","d")
else :
    print("학점:","F")