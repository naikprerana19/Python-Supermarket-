print("🛍 Welcome to Python Supermarket 🛍")

products = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 40,
    "eggs": 80
}

cart = {}

def show_products():
    print("\n📦 Available Products:")
    print("-" * 30)
    for item, price in products.items():
        print(f"{item:<10} ₹{price}")
    print("-" * 30)

def add_to_cart():
    item = input("Enter product name: ").lower()
    if item in products:
        try:
            qty = int(input(f"Enter quantity of {item}: "))
            if qty <= 0:
                print("❌ Quantity must be positive!")
                return
            cart[item] = cart.get(item, 0) + qty
            print(f"✅ {qty} {item}(s) added to cart.")
        except ValueError:
            print("❌ Invalid quantity.")
    else:
        print("❌ Product not found!")

def view_cart():
    if not cart:
        print("\n🛒 Your cart is empty!")
        return

    print("\n🛒 Your Cart:")
    print("-" * 40)
    total = 0
    for item, qty in cart.items():
        price = products[item] * qty
        total += price
        print(f"{item:<10} x{qty:<3} = ₹{price}")
    print("-" * 40)

    # 🎁 Discount logic
    discount = 0
    if total >= 500:
        discount = total * 0.10  # 10% discount
        print(f"🎉 Discount Applied: ₹{discount:.2f}")

    grand_total = total - discount
    print(f"🧾 Total Payable: ₹{grand_total:.2f}")

def remove_item():
    item = input("Enter item to remove: ").lower()
    if item in cart:
        del cart[item]
        print(f"🗑 {item} removed from cart.")
    else:
        print("❌ Item not found in cart.")

def checkout():
    if not cart:
        print("🛒 Cart is empty! Add something before checkout.")
        return

    print("\n🧾 --- BILL RECEIPT ---")
    total = 0
    for item, qty in cart.items():
        cost = products[item] * qty
        total += cost
        print(f"{item:<10} x{qty:<3} = ₹{cost}")

    discount = 0
    if total > 500:
        discount = total * 0.10
    grand_total = total - discount

    print("------------------------------")
    print(f"Subtotal: ₹{total}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Total: ₹{grand_total:.2f}")
    print("✅ Payment successful. Thank you for shopping! 💳")
    cart.clear()  # empty cart after checkout

# 🧭 Main menu
while True:
    print("\n📋 MENU:\n⿡ Show Products\n⿢ Add to Cart\n⿣ View Cart\n⿤ Remove Item\n⿥ Checkout\n⿦ Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        checkout()
    elif choice == "6":
        print("👋 Thank you for visiting Python Supermarket!")
        break
    else:
        print("❌ Invalid choice. Try again.")

