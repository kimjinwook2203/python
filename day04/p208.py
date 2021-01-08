print('start');## 스트링 리스트?
cart = [];

def viewCart(c):
    ptotal = 0;  # 값과 갯수
    ctotal = 0;
    for item in c:
        print('Item: %s %d %d' % (item[0], int(item[1]), int(item[2])));
        ptotal += int(item[1])
        ctotal += int(item[2])
    print('total: %d %d' % (ptotal, ctotal));

while True:
    menu = input('Input menu(i,v,r,q)');
    if menu == 'i':
        item = input('Input Item(name,price,count)');
        item = item.split(' '); # ['',1000,1]
        cart.append(item);
    if menu == 'v':
        viewCart(cart);
    if menu == 'r':
        itemname = input('Input item name')
        for citem in cart:
            if itemname in citem:
                cart.remove(citem);
                print(citem[0]+'삭제되었습니다.');

    if menu == 'q':
        print('bye')
        break;
print('end')