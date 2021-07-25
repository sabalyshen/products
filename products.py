#檢查有沒有之前的檔案
import os # 載入作業系統operating system
games = []
if os.path.isfile('products.csv'):
    print('讀取以前檔案')
    with open('products.csv', 'r', encoding = 'utf-8') as f:
	    for line in f:
	    	if '遊戲, 價格' in line:
	    		continue # 跳到下一個迴圈
	    	name, price = line.strip().split(',') 
    		games.append([name, price])
    print(games)
else:
	print('歡迎!初次使用')

while True:
	name = input('請輸入遊戲名稱: ')
	if name == 'q':
		break
	price = input('請輸入遊戲價格: ')
	price = int(price)
	games.append([name, price])
print(games)

for g in games:
	print(g) 
	print(g[0]) 

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('遊戲, 價格\n') #加入欄位名稱
	for g in games:
		f.write(g[0] + ',' + str(g[1]) + '\n') 