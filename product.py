 #檢查檔案在不在
import os
products = []
if os.path.isfile("product.csv"): 
	print("耶找到檔案了")
	with open("product.csv", "r", encoding= "utf-8") as f:
		for line in f:
			if "商品,價格" in line:
				continue
			name,price = line.strip().split(",")
			products.append([name,price])
	print(products)

else:
	print("沒有相關檔案")
 




while True:
	name = input("請輸入商品名稱:")
	if name == "q":
		break
	price = input("請輸入商品價格：")
	price = int(price)
	p = [name,price]
	"""
	P = []
	P.append(name)
	P.append(price)
	"""
	products.append(p)
print(products)

for p in products:
	print(p[0],"的價格是", p[1])

#寫入檔案
with open("product.csv", "w",encoding="UTF-8") as f:
	f.write("商品,價格\n")
	for p in products:
		f.write(str(p[0]) + "," + str(p[1]) + "\n")

