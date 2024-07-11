class Order:
    def __init__(self):
        self.menu = {
            'beef': {'small': 80, 'medium': 95, 'large': 110},
            'chicken': {'small': 75, 'medium': 90, 'large': 105},
            'seafood': {'small': 110, 'medium': 135, 'large': 150},
            'pepperoni': {'small': 70, 'medium': 90, 'large': 115}
        }
        self.order = []
    
    def display_menu(self):
        for pizza, info in self.menu.items():
            print(f"{pizza}: ", end='')
            for size, price in info.items():
                print(f"size {size} costs {price} ", end='')
            print()
    
    def add_pizza(self, pizza_name, size):
        if pizza_name not in self.menu or size not in self.menu[pizza_name]:
            print("Not valid")
            return
        self.order.append([pizza_name, size])
    
    def calculate_total_cost(self):
        print("Your Order: ")
        total_cost = 0
        for pizza_name, size in self.order:
            print(f"- {size} {pizza_name} pizza")
            total_cost += self.menu[pizza_name][size]
        print(f"Total cost is: {total_cost}")
        self.order.clear()

print("Welcome to out pizza app")
print("Here are our pizza options")
pizza = Order()
pizza.display_menu()

while True:
    name = input("Enter pizza name or type \"done\" to finsish your order: ")
    name = name.lower()
    if name == 'done':
        pizza.calculate_total_cost()
        con = input("Would you like to place another order? (yes/no): ")
        if con == "no":
            print("Thank you for ordering from our pizza app!")
            break
        continue
    size = input("Enter the size (small, medium, large): ")
    size = size.lower()
    pizza.add_pizza(name, size)
