
class Invoice:
    
    def __init__(self):
        self.items = {}
    
    def add_product(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    
    def total_impure_price(self, products):
        total_impure_price = 0
        
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price


    def total_discount(self, products):
        total_dis = 0
        for k, v in products.items():
            total_dis += (int(v['qnt']) * float(v['unit_price'])) * float (v['discount']) / 100
        total_dis = round(total_dis, 2)
        self.total_dis = total_dis
        return total_dis
    
    
    def total_pure_price(self, products):
        total_pure_price = self.total_impure_price(products) - self.total_discount(products)
        return total_pure_price
    
    def input_answer(self, input_value):
        while True:
            user_input = input(input_value)
            if user_input in ['y', 'n']:
                return user_input
            print('y or n! Try again.')
            
    
    def input_number(self, input_value):
        while True:
            try:
                user_input = float(input(input_value))
            except ValueError:
                print("Not a number! Try agian.")
                continue
            else:
                return user_input