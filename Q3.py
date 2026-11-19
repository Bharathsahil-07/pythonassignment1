order_amount = float(input("Enter order amount (in Rs): "))
membership = input("Are you a member? (yes/no): ")
is_member = membership.strip().lower() == "yes"
is_valid_amount = order_amount >= 0 and order_amount <= 100000
if not is_valid_amount:
    print("Invalid order amount. Amount must be between Rs 0 and Rs 1,00,000.")
else:
    if order_amount >= 5000:
        discount_percent = 15
        eligibility = "Eligible: 15% discount for order of Rs 5,000 or more"
    elif is_member and order_amount >= 2000:
        discount_percent = 10
        eligibility = "Eligible: 10% member discount"
    else:
        discount_percent = 0
        eligibility = "Not eligible for any discount"
    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount
    print("Original amount :", format(order_amount, ",.2f"))
    print("Discount        :", discount_percent, "%")
    print("Discount amount :", format(discount_amount, ",.2f"))
    print("Final payable   :", format(final_amount, ",.2f"))
    print("Status          :", eligibility)