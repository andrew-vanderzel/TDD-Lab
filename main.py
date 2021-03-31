from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''

while True:
    product = input('What is your product : ')
    unit_price = Invoice().input_number("Please enter unit price: ")
    qnt = Invoice().input_number("Please enter quantity of product: ")
    discount = Invoice().input_number("Discount percent (%): ")
    repeat = Invoice().input_answer("Another product? (y/n):")
    result = Invoice().add_product(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break
    
total_amount = Invoice().total_pure_price(products)
print("Your total pure price is:", total_amount)
    