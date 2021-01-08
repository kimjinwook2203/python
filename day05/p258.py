from random import randint as rdt;
import myutil1 as m1;# 쉽게 쓸고
import myutil2;


a = 100;
b = rdt(1,10);
print(a,b);
print(m1.sum(a,b));
print(myutil2.sum(a,b))