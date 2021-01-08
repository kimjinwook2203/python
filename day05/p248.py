#map
#filter처럼 뭔가를 꺼내는게 아니라 전부 사용하는거
def mymap(n):
    return n/2;
score = [90,80,60,100];

for i in map(mymap, score): # score에 있는 점수를 다 적용할거야
    print(i);

print('-----------------------------')

for i in map(lambda x:x/3,score):
    print(i);
