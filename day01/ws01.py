a = input('숫자를 입력 하세요')
b = input('숫자를 입력 하세요')
c = input('숫자를 입력 하세요')
try :
    num1 = int(a)
    num2 = int(b)
    num3 = int(c)
except :
    print("숫자를 입력하세요.")
    exit()

sum = int(a) + int(b) + int(c)
avg = round(sum/ 3, 1)


print(sum)
print(avg)