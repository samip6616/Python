price = 250
quantity = 5
discount_rate = 0.10
tax_rate = 0.13

subtotal = price * quantity
discounted = subtotal * (1 - discount_rate)
total = discounted * (1 + tax_rate)

print(total)