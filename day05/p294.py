d = 'a';
result = '0'

try:
    num =int(d);
    result = 10 / num;

except ValueError as e: # 어떤 에러인지 보여주려고
    print(e);
    print('invalid input character')
    exit()
except ZeroDivisionError:
    print('zero division error')
    exit()


print(result);