a = 1;
b = a;
print('a:%d b:%d' % (a,b));

a= 5;
print('a:%d b:%d' % (a,b));


list1 = [1,2,3,4];
list2 = list1;#이거는 주소가 들어간다
list3 = list1.copy();#카피를 하면 값이 들어가고

print(list1);
print(list2);

print('-------------------------');
list1[0] = 100;
print(list1);
print(list2);
print(list3);

