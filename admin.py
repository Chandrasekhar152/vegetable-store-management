veg = ["tomato", "potato", "carrot", "onion", "cabbage"]

prices = [40, 30, 50, 35, 45]

quantity = [10, 20, 15, 25, 12]

selling_prices = [50, 40, 60, 45, 55]



while True:

    print("ADMIN MENU")
    print("1. Add Vegetable")
    print("2. View Vegetables")
    print("3. Exit")

    admin_choice = int(input("Choose your choice 1 or 2 or 3: "))
    
    if admin_choice==1:
        admin_vegies=input("Enter the Vegie name that you want to add: ").lower()
        
        if admin_vegies in veg:
            print(f'The {admin_vegies} was already in store')
            admin_modify = input('Do you want to modify price/quantity/selling_price/remove ').lower()

            #remove vegies from store

            if admin_modify=='remove':
                index = veg.index(admin_vegies)
                print(f'The current price for the {veg[index]} is {prices[index]}')
                remove_confirm = input(f'Are you sure you want to remove {veg[index]} from the store? (yes/no): ').lower()
                if remove_confirm == 'yes':
                    veg.pop(index)
                    prices.pop(index)
                    quantity.pop(index)
                    selling_prices.pop(index)
                    print(f'{admin_vegies} has been removed from the store.')
                    


            if admin_modify == 'selling_price':
                print(f'The current selling price for the {admin_vegies} is {selling_prices[veg.index(admin_vegies)]}')
                print('Do you want to (1.replace, 2.increase, 3.decrease) choose 1 or 2 or 3')
                admin_modify_selling_price = input('Enter your choice: ').lower()

                if admin_modify_selling_price == 'replace' or admin_modify_selling_price == '1':
                    index = veg.index(admin_vegies)
                    print(f'The current selling price for the {veg[index]} is {selling_prices[index]}')
                    selling_price = int(input("Enter the amount: "))
                    if selling_price >= 0:
                        selling_prices[index] = selling_price
                    else:
                        print("Selling price cannot be negative.")
                    print(f'The current selling price for the {veg[index]} is changed to {selling_prices[index]}')
                
                elif admin_modify_selling_price=='increase' or admin_modify_selling_price=='2':
                    index = veg.index(admin_vegies)
                    print(f'The current selling price for the {veg[index]} is {selling_prices[index]}')
                    selling_price_increase = int(input("Enter the increase amount: "))                   
                    selling_prices[index] = selling_prices[index] + selling_price_increase
                    print(f'The current selling price for the {veg[index]} is changed to {selling_prices[index]}')
                
                elif admin_modify_selling_price=='decrease' or admin_modify_selling_price=='3':
                    index = veg.index(admin_vegies)
                    print(f'The current selling price for the {veg[index]} is {selling_prices[index]}')
                    selling_price_decrease = int(input("Enter the decrease amount: ")) 
                
                    if 0 <= selling_prices[index] - selling_price_decrease:
                        selling_prices[index] = selling_prices[index] - selling_price_decrease
                    else:
                        print(f'The selling price will become negative: {selling_prices[index] - selling_price_decrease}')

                    print(f'The current selling price for the {veg[index]} is changed to {selling_prices[index]}')

            #Price Modification

            if admin_modify == 'price':
                index = veg.index(admin_vegies)
                print(f'The current price for the {veg[index]} is {prices[index]}')

                admin_modify_price = input('Do you want to (1.replace, 2.increase, 3.decrease) choose 1 or 2 or 3').lower()
                if admin_modify_price == 'replace' or admin_modify_price == '1':
                    print(f'The current price for the {veg[index]} is {prices[index]}')
                    price = int(input("Enter the amount: "))
                    if price >= 0:
                        prices[index] = price
                    else:
                        print("Price cannot be negative.")
                    print(f'The current price for the {veg[index]} is changed to {prices[index]}')

                elif admin_modify_price=='increase' or admin_modify_price=='2':
                    print(f'The current price for the {veg[index]} is {prices[index]}')
                    price_increase = int(input("Enter the increase amount: "))                   
                    prices[index] = prices[index] + price_increase
                    print(f'The current price for the {veg[index]} is changed to {prices[index]}')

                elif admin_modify_price=='decrease' or admin_modify_price=='3':
                    print(f'The current price for the {veg[index]} is {prices[index]}')
                    price_decrease = int(input("Enter the decrease amount: "))
                    if 0<=prices[index] - price_decrease:               
                        prices[index] = prices[index] - price_decrease
                    else:
                        print(f'The price will become negative: {prices[index] - price_decrease}')
                    print(f'The current price for the {veg[index]} is changed to {prices[index]}')
                
        
            #Quantity modification
            if admin_modify == 'quantity':
                index = veg.index(admin_vegies)
                print(f'The current quantity for the {veg[index]} is {quantity[index]}')

                admin_modify_quantity = input('Do you want to (1.replace, 2.increase, 3.decrease) choose 1 or 2 or 3').lower()
                if admin_modify_quantity == 'replace' or admin_modify_quantity == '1':
                    print(f'The current quantity for the {veg[index]} is {quantity[index]}')
                    new_quantity = int(input("Enter the amount: "))
                    if new_quantity >= 0:
                        quantity[index] = new_quantity
                    else:
                        print("Quantity cannot be negative.")
                    print(f'The current quantity for the {veg[index]} is changed to {quantity[index]}')
                
                elif admin_modify_quantity=='increase' or admin_modify_quantity=='2':
                    print(f'The current quantity for the {veg[index]} is {quantity[index]}')
                    quantity_increase = int(input("Enter the increase quantity: "))                   
                    quantity[index] = quantity[index] + quantity_increase
                    print(f'The current quantity for the {veg[index]} is changed to {quantity[index]}')

                elif admin_modify_quantity=='decrease' or admin_modify_quantity=='3':
                    print(f'The current quantity for the {veg[index]} is {quantity[index]}')
                    quantity_decrease = int(input("Enter the decrease amount: "))
                    
                    if 0<=quantity[index] - quantity_decrease:               
                        quantity[index] = quantity[index] - quantity_decrease
                    else:
                        print(f'The quantity will become negative: {quantity[index] - quantity_decrease}')
                    print(f'The current quantity for the {veg[index]} is changed to {quantity[index]}')

        

        elif admin_vegies not in veg:
            admin_price = int(input(f'Enter the price for {admin_vegies}: '))
            admin_quantity = int(input(f'Enter the quantity for {admin_vegies}: '))
            admin_selling_price = int(input(f'Enter the selling price for {admin_vegies}: '))

            veg.append(admin_vegies)
            prices.append(admin_price)
            quantity.append(admin_quantity)
            selling_prices.append(admin_selling_price)


            
    elif admin_choice==2:
        print("THE VEGETABLES IN STORE ARE:")
        for items in zip(veg,prices,quantity,selling_prices):
            print(f'Vegetable: {items[0]:<10}| Price: {items[1]:<10}| Quantity: {items[2]:<10}| Selling Price: {items[3]:<10}')
    elif admin_choice == 3:
        print("You just logout")
        break
    else:
        print("Invalid choice")

print("Thank you for using the system")