import sys;

print(sys.version);
print(sys.platform);

data = input('Input number...?');
print('input number:'+str(data));

#terminal 들어가서 외부 인스톨 pip install
#pip install 을 치면 외부 라이브러리를 현재 파이썬에 탑재 할 수 있다
#pip install pyinstaller를 설치
#pyistaller -F p282.py 윈도우에서 돌아가는 실행파일
