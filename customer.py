veg = ["Tomato", "Potato", "Carrot", "Onion", "Cabbage"]

prices = [40, 30, 50, 35, 45]

quantity = [10, 20, 15, 25, 12]


while True:
    print('1. Adding Vegies with quantiy with prices')
    print('2. View vegies from store')
    print('3. Enter 3 to exit')

    admin_choice = int(input("Choose your choice 1 or 2 or 3 "))
    
    if admin_choice==1:
        admin_vegies=input("Enter the Vegie name that you want to add: ")
        admin_price = int(input("Enter the price name for vegitable: "))
        admin_quantity = int(input('enter the quantity: '))
        
        if admin_vegies not in veg:
            veg.append(admin_vegies)
            prices.append(admin_price)
            quantity.append(admin_quantity)
        
        elif admin_vegies in veg:
            print(f'The {admin_vegies} was already in store')
            admin_modify = input('Do you want to modify price/quantity/remove? ').lower()

            #Price Modification

            if admin_modify == 'price':
                index = veg.index(admin_vegies)
                print(f'The current price for the {veg[index]} is {prices[index]}')

                admin_modify_price = input('Do you want to (1.replace, 2.increase, 3.decrease, 4.remove) choose 1 or 2 or 3 or 4').lower()
                if admin_modify_price=='replace' or admin_modify_price=='1':
                    print(f'The current price for the {veg[index]} is {prices[index]}')
                    prices[index] = int(input("Enter the amount: "))
                    print(f'The current price for the {veg[index]} is changed to {prices[index]}')

                elif admin_modify_price=='increase' or admin_modify_price=='2':
                    print(f'The current price for the {veg[index]} is {prices[index]}')
                    price_increase = int(input("Enter the increase amount: "))                   
                    prices[index] = prices[index] + price_increase
                    print(f'The current price for the {veg[index]} is changed to {prices[index]}')

                elif admin_modify_price=='decrease' or admin_modify_price=='3':
                    print(f'The current price for the {veg[index]} is {prices[index]}')
                    price_decrease = int(input("Enter the decrease amount: "))                    
                    prices[index] = prices[index] - price_decrease
                    print(f'The current price for the {veg[index]} is changed to {prices[index]}')
                
                #remove vegies from store
                
            elif admin_modify_price=='remove' or admin_modify_price=='4':
                index = veg.index(admin_vegies)
                print(f'The current price for the {veg[index]} is {prices[index]}')
                remove_confirm = input(f'Are you sure you want to remove {veg[index]} from the store? (yes/no): ').lower()
                if remove_confirm == 'yes':
                    veg.pop(index)
                    prices.pop(index)
                    quantity.pop(index)
                    print(f'{admin_vegies} has been removed from the store.')

            #Quantity modification
            if admin_modify == 'quantity':
                index = veg.index(admin_vegies)
                print(f'The current quantity for the {veg[index]} is {quantity[index]}')

                admin_modify_quantity = input('Do you want to (1.replace, 2.increase, 3.decrease) choose 1 or 2 or 3').lower()
                if admin_modify_quantity=='replace' or admin_modify_quantity=='1':
                    print(f'The current quantity for the {veg[index]} is {quantity[index]}')
                    quantity[index] = int(input("Enter the amount: "))
                    print(f'The current quantity for the {veg[index]} is changed to {quantity[index]}')

                elif admin_modify_quantity=='increase' or admin_modify_quantity=='2':
                    print(f'The current quantity for the {veg[index]} is {quantity[index]}')
                    quantity_increase = int(input("Enter the increase quantity: "))                   
                    quantity[index] = quantity[index] + quantity_increase
                    print(f'The current quantity for the {veg[index]} is changed to {quantity[index]}')

                elif admin_modify_quantity=='decrease' or admin_modify_quantity=='3':
                    print(f'The current quantity for the {veg[index]} is {quantity[index]}')
                    quantity_decrease = int(input("Enter the decrease amount: "))                    
                    quantity[index] = quantity[index] - quantity_decrease
                    print(f'The current quantity for the {veg[index]} is changed to {quantity[index]}')

    elif admin_choice==2:
        print("THE VEGETABLES IN STORE ARE:")
        for items in zip(veg,prices,quantity):
            print(f'Vegetable: {items[0]:<10}, Price: {items[1]:<10}, Quantity: {items[2]:<10}')
    elif admin_choice == 3:
        print("You just logout")
        break
    else:
        print("Invalid choice")

print("Thank you for using the system")
