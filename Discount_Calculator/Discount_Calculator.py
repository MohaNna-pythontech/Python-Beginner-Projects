price = float(input("Enter purchase amount: "))
if price > 1000:
    discount = price * 70 / 100
    final_price = price - discount
    print("Final price: ",  final_price)
else:
       print("No discount")
       print("Final price:",price)