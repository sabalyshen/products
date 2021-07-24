#二維清單(2 dimensional): 清單中的清單
products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
    	break
    price = input('請輸入商品價格: ')
    p = []
    p.append(name)
    p.append(price)
    products.append(p) 
# products(大清單)每一個清單裝入name & price這兩個小清單
print(products)
# SO 會印出 [['name', 'price'], ['name', 'price'], ......]

products[0][0]
#第一個[0]就是大清單的第0格
#第二個[0]就是大清單中的小清單的第0格