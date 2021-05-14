products = []
while True:
	name = input("請輸入商品名稱:")
	if name == "取消":
		break
	price = input("請輸入商品價格：")
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
