list = []
for n in range(0,100,5) :
    list.append(n); ## append 는 나중에 배우는거 하지만 list 에 넣는그런 의미 인듯

print(len(list));
print(list);

for n in range (1,11) :
    if n % 2 == 1:
        continue;
    print(n);