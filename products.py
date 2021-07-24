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
# p = [name, price] 即可完成上面3行
    products.append(p) 
#products.append([name, price]) 即可完成上面4行

# products(大清單)每一個清單裝入name & price這兩個小清單
print(products)
# SO 會印出 [['name', 'price'], ['name', 'price'], ......]

products[0][0]
#第一個[0]就是大清單的第0格
#第二個[0]就是大清單中的小清單的第0格

#final
game = []
while True:
	game_name = input('請輸入遊戲名稱: ')
	if game_name == 'q':
		break
	game_cost = input('請輸入遊戲價格: ')
	game.append([game_name, game_cost])
print(game)