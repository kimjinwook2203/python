#lotto Game
#뒷부분 마무리는 아직 미흡하여 마무리 못했습니다.죄송합니다.

#1) 당첨번호 6개 랜덤으로 생성하기
#2) 응모자로부터 입력값 받아들이기
#3) 당첨번호와 응모 번호 비교 후 당첨 여부 확인

print('game start');
import random;
##0) 당첨금
prize = [];
for i in range(1,6):
    pt = random.randint(5000,30000);
    prize.append(pt);
    prize.sort()
print ('당첨금 1등:%d원 2등:%d원 3등:%d원 4등:%d원 5등:%d원' % (prize[4],prize[3],prize[2],prize[1],prize[0]))
##1) 당첨번호 6개 랜덤으로 생성하기
randnum=[];

for i in range(1,7):
    temp = random.randint(1,45);
    randnum.append(temp);
    randnum.sort()
print ('당첨번호 :',randnum);

##2) 응모자로부터 입력 값 받아들이기
usernum =[];

usernum = input('숫자 입력하세요');
usernum = usernum.split(' ');
usernum = list(map(int, usernum))
usernum.sort()

#3) 당첨번호와 응모 번호 비교 후 당첨 여부 확인
#여기는 어떻게 하는지 도저히 몰라서 내일 공부하겠습니다.
print(usernum)
if usernum == randnum :
    print('1등')