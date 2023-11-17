from random import choice

flavours = ["strawberry", "chocolate", "vanilla", "rum raisin", "raspberry ripple"]

for i in range(10):
    print(f"ice cream choice = {choice(flavours)}")
