import random;

prize = []
for i in range(1,6):
    pt = random.randint(5000,30000);
    prize.append(pt);
    prize.sort()

print(prize)
print(prize[4])