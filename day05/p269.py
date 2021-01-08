import time;

i= 1;


while True:
    print('try connect...');
    i+=1;

    if i == 10:
        print('connect success');
        break;
    time.sleep(0.5)

    print('retry')
    i += 1;