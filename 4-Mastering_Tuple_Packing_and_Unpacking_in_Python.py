# Task 1: Customer Order Processing

orders = [ # Given orders
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Santa", "Sled", 1),
    ("Dave", "Screwdriver", 4)
]

def printOrders(): # Function to print all orders
    for order in orders: # Loop through each order
        name, product, quantity = order # Unpack tuple for easier formatting
        if quantity > 1: # Use plural if quantity is more than 1
            print(f"{name} ordered {quantity} {product.lower()}s.")
        else: 
            print(f"{name} ordered a {product.lower()}.")

printOrders()