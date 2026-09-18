veg = ["tomato", "potato", "carrot", "onion", "cabbage"]
prices = [40, 30, 50, 35, 45]
quantity = [10, 20, 15, 25, 12]
selling_prices = [50, 40, 60, 45, 55]

user_cart = []
user_cart_quantity = []
user_cart_price = []


print('==========WELCOME TO VEZZIES STORE==========')
while True:
    print("1.To view the available vegetables")
    print("2.To buy vegetables")
    print('3.TO see your card')
    print('4.To remove items from cart')
    customer_choice = int(input('Enter your choice: '))

    if customer_choice == 1:
        print('The available vegetables are:')
        for items in zip(veg,prices,quantity, selling_prices):
            print(f'Vegtable Name: {items[0]:<10} | Avi Quantity {items[2]} | Selling Price: {items[3]:<10}per Kg')

    elif customer_choice == 2:
        print('The available vegetables are:')
        for items in zip(veg,prices,quantity, selling_prices):
            print(f'Vegtable Name: {items[0]:<10} | Avi Quantity {items[1]} | Selling Price: {items[2]:<10}per Kg')
        
        while True:
            user_vegies = input('Enter the vegetable name you want to buy: ').lower()
            if user_vegies in veg:
                index =veg.index(user_vegies)
                user_cart_quantity_choice=(int(input('Enter the quantity you want to buy: ')))
                if user_cart_quantity_choice <= quantity[index]:
                    user_cart.append(user_vegies)
                    user_cart_quantity.append(user_cart_quantity_choice)
                    quantity[index] = quantity[index] - user_cart_quantity_choice
                    user_cart_price.append(selling_prices[index])
                else:
                    print(f'Sorry, we only have {quantity[index]} kg of {user_vegies} available.')
                
                for i in zip(user_cart, user_cart_quantity, user_cart_price):
                    print(f'Vegtable Name: {i[0]:<10} | Quantity: {i[1]} | Price: {i[2]:<10}per Kg')
                print('Do you want to buy more vegetables? (yes/no)')
                user_choice = input('Enter your choice: ').lower()
                if user_choice == 'no':
                    print('Your cart is:')
                    for i in zip(user_cart, user_cart_quantity, user_cart_price):
                        print(f'Vegtable Name: {i[0]:<10} | Quantity: {i[1]} | Price: {i[2]:<10}per Kg')
                    break

    elif customer_choice==3:
        print("YOUR CART IS BELOW")
        for items in zip (user_cart, user_cart_quantity, user_cart_price):
            print(f'Vegtable Name: {items[0]:<10} | Quantity: {items[1]} | Price: {items[2]:<10}per Kg')

    
    elif customer_choice==4:
        print('Enter the vegtable name to remove from cart: ')
        while True:
            user_remove_choice = input("")
            index = user_cart.index(user_remove_choice)
            print(f"Your cart have {user_cart[index]} with qantity of {user_cart_quantity[index]}")
            print("Please enter valid quantity to remove selected vegtable: ")
            print("DO YOU WANT TO REDUCE QUANTITY OR REMOVE VEGGIES FROM CART")
            print("Cick 1.To remove veggie from cart")
            print("Click 2. To Remove Quantity")
            user_remove_option = int(input("Enter your choice: "))

            if user_remove_option == 2:
                user_quantity_choice = int(input())
                if user_cart_quantity[index]-user_quantity_choice > 0:
                    user_cart_quantity[index] = user_cart_quantity[index]-user_quantity_choice
                elif user_cart_quantity[index]-user_quantity_choice == 0:
                    user_cart.pop(index)
                    user_cart_price.pop(index)
                    user_cart_quantity.pop(index)
                else:
                    print("Please enter valid quantity to remove selected vegtable: ")
            elif user_remove_option == 1:
                    user_cart.pop(index)
                    user_cart_price.pop(index)
                    user_cart_quantity.pop(index)