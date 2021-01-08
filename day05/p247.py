#filter

def myfilter1(n):
    return n >= 90;#90보다 클때만 return

def myfilter2(n):
    return n >= 80;



score = [90,80,60,100];

#for i in score :
#    if i>= 90:
#        print(i);

for i in filter(myfilter2, score):#list를 필터할건데 마이 필터 기능을 가져갈거야
    print(i)

print('--------------------------')

for i in filter(lambda x:x>=90, score):
    print(i);