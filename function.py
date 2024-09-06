# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price or original price if no discount was applied
if final_price == original_price:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
else:
    print(f"Discount applied! The final price is: ${final_price:.2f}")
