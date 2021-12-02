no_of_books = int(input("How many books do you have in your basket? "))


price = float(input(f"What is the price of the book number 1? "))
total = price
min_price = price
max_price = price
cheaper_than_10 = 0
if price < 10.0:
   cheaper_than_10 += 1

for data in range(2, no_of_books + 1):
   price = float(input(f"What is the price of the book number {data}? "))

   total += price
   average = total / no_of_books
   if price < min_price:
      min_price = price
   if price > max_price:
      max_price = price
   if price < 10.0:
      cheaper_than_10 += 1
   percentage = (cheaper_than_10 / no_of_books)* 100
   
print(f"Total price: {total}")
print(f"Average price: {average:.2f}")
print(f"Price of the least expensive book: {min_price}")
print(f"Price of most expensive book: {max_price}")
print(f"Number of books cheaper than $10: {cheaper_than_10}")
print(f"Percentage of books cheaper than $10: {percentage:.2f}%")