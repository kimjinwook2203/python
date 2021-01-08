s = [];
s.append(20);
s.append(30);
s.append(10);
s.append(40);
s.append(50);
s.insert(2,99); # 2번째에 99를 집어 넣는다.
s[3] = [1,2,3];
del(s[0]);
s.remove(50);#위치를 안잡아주고 50이라는 값을 지움 알아서 찾아서
print(s.pop());
print(s.pop(1));#pop은 list의 맨 뒤 끄집어 내는거
print(s.index(30));#30이 몇번쨰야 ??
s.append(30);
print(s.count(30));#30 이 몇개 있어?
print(s);

str = ['a' , 'b', 'c', 'd', 'd'];

if 'a' in str: # str 안에 a  있으면
    str.remove('a');
else:
    str.append('a');
print(str);