veg =[]
prices = []
quantity = []


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
            admin_modify = input('Do you want to modify price/qantity').lower()

            #Price Modification

            if admin_modify == 'price':
                index = veg.index(admin_vegies)
                print(f'The current price for the {veg[index]} is {prices[index]}')

                admin_modify_price = input('Do you want to (1.replace, 2.increase, 3.decrease) choose 1 or 2 or 3').lower()
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
        for items in zip(veg,prices,quantity):
            print(items)
    elif admin_choice == 3:
        print("You just logout")
        break
    else:
        print("Invalid choice")