# Create a dictionary for flower bulbs
flower_bulbs = {
    'daffodil': 0.35,
    'tulip': 0.33,
    'crocus': 0.25,
    'hyacinth': 0.75,
    'bluebell': 0.50
}

# Mary's standing order
mary_order = {
    'daffodil': 50,
    'tulip': 100
}

# Update the price of tulip bulbs
flower_bulbs['tulip'] *= 1.25
flower_bulbs['tulip'] = round(flower_bulbs['tulip'], 2)

# Add hyacinth bulbs to Mary's order
mary_order['hyacinth'] = 30

# Display Mary's purchase order
print("You have purchased the following bulbs:")
for bulb_name, quantity in sorted(mary_order.items()):
    code = bulb_name[:3].upper()
    price_per_bulb = flower_bulbs[bulb_name]
    subtotal = quantity * price_per_bulb
    print(f"{code} * {quantity:4} = $ {subtotal:6.2f}")

# Calculate total number and cost
total_bulbs = sum(mary_order.values())
total_cost = sum(mary_order[bulb] * flower_bulbs[bulb] for bulb in mary_order)

# Display total information
print(f"\nThank you for purchasing {total_bulbs} bulbs from Bluebell Greenhouses.")
print(f"Your total comes to $ {total_cost:6.2f}.")
