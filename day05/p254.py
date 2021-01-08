a= 1;
b= a;

if (a==b):
    print('ok1');

if (a is b): # is 는 두개의 메모리 위치를 비교 하는것
    print('ok2');


print('-------------------------');

d1 = [1,2,3];
d2 = d1;

if (d1== d2):
    print('list ok1');
if (d1 is d2):
    print('list ok2');