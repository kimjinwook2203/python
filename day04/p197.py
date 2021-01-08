score = []; # 아무것도 없는 list
score1 = [10, 20, 30,40,50,60,70,80];

print(score1[1:5]);
temp = score1[1:5:2];#list를 2칸씩
print(temp); #list에서 짤라내도 list가 된다.

sum= 0;
for i in score1:
    sum +=i;

print('result : %d %f' % (sum,sum/len(score1)));

score2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]];
#print(score2[1][3]);

sum2= 0;
avg = 0;

for i1 in score2:
    for i2 in i1:
        sum2 +=i2;
        avg = sum2/len(i1)
        print (sum2,avg)
    print();

#각 리스트의 합 평균을 출력하고
#전체 합과 평균을 출력 하시오


total = 0;
totalcnt = 0;
for i1 in score2:
    sum = 0;
    cnt = len(i1);
    for i2 in i1:
        sum += i2;
    print('%d %.2f' % (sum, sum/cnt));
    total += sum;
    totalcnt += cnt;
print ('%d %.2f' % (total, total/totalcnt));

