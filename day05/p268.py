import time;
###얼마나 시간 걸렸는지 계산해보는것

start = time.time();#1970년대를 기준으로 현 시점까지 시단

for i in range(1,100):
    print(i);
    time.sleep(0.05)
end = time.time();
print(end-start);


