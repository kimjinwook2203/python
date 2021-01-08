import myutil1;

d = 0;
try:
    result = myutil1.calc(d);
    print(result);
except ZeroDivisionError:
    print('Zero division error')
    exit()
