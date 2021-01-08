score = (10,20,30,40);
score = score + (50, 60, 70); #score
print(score);
scorelist = list(score); #tuple이 list로 바뀐다

import random;

t=[];
for i in range(1,7):
    temp = random.randint(1,45);
    t.append(temp);

print(t)