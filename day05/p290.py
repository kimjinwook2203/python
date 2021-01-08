
#a = input('input number..?');
#result = 0;
#if a.isdecimal()== True:# a 가 숫자면
#    result = int(a)/2
#else:
#    print('invalid input character')

#print(result);

#예외사항
a=input('input numer..?');
result = 0;
try:
    result = 2/ int(a);
except:
    print('invalid input number')
    exit(); # 이 다음문장들이 실행 될 필요가없으니가 프로그램 종료
print(result);