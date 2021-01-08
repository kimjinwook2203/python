data ="adadadsdajkdnjvnv hraor a vainrioan v aoowqiroqwutubnnvmx cvklnzoinwenbgkjabgsjdboua htjkbjbjhvciusdhantiojvkxlnklvmxzviohqihrgwyrgqjjwropjasdhjbcjzbvjbzlkvmlakorwqothjhdsad"

temp = 'abc def ghi'
count = {};
for c in data:
    if c.isalpha()==False:
        continue;
    c = c.lower();

    if c not in count:
        count[c] = 1;
    else :
        count[c] +=1;

print(count.items());
result = sorted(count.items(), key=lambda x:x[1], reverse=True); #튜플들을 가지고 1번째를 기준으로 숫자가 많은 순으로 0번부터 5번
print(result[0:5]);