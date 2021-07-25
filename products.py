#二維清單(2 dimensional): 清單中的清單
"""
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
"""

#final
games = []
while True:
	game_name = input('請輸入遊戲名稱: ')
	if game_name == 'q':
		break
	game_cost = input('請輸入遊戲價格: ')
	game_cost = int(game_cost)
	games.append([game_name, game_cost])
print(games)

for g in games:
	print(g) # 依序印出大清單(games)的東西
	print(g[0]) # 依序印出大清單(games)中的第一個小清單
"""
for c in game_cost:
	print(c) #for loot 走到最後的值
"""

# 字串可以+-*/
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f:
# csv 可用excel打開，多個清單好用
	f.write('遊戲, 價格\n') #加入欄位名稱
	for g in games:
		f.write(g[0] + ',' + str(g[1]) + '\n') #str = string 數字改為字串字串
# csv 每一格格子用 ',' 區隔