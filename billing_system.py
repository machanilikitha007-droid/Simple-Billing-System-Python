items = []

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    items.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })

    print("Item added successfully!")


def generate_bill():
    if not items:
        print("No items added.")
        return

    print("\n========== BILL ==========")

    total = 0

    for item in items:
        amount = item["quantity"] * item["price"]

        print(
            item["name"],
            "x",
            item["quantity"],
            "= ₹",
            amount
        )

        total += amount

    print("--------------------------")
    print("Total Amount: ₹", total)


while True:
    print("\n===== SIMPLE BILLING SYSTEM =====")
    print("1. Add Item")
    print("2. Generate Bill")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        generate_bill()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
