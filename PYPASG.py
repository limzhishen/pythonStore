# LAU ZI YAN
# TP064326
import time

# Print Plenty of \n [nextline] to clear the screen 
ClearPage = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'''

WELCOMENOTE = '''
  ______ _____  ______  _____ _    _  _____ ____     _____     _         ____  _         _ 
 |  ____|  __ \|  ____|/ ____| |  | |/ ____/ __ \   / ____|   | |       |  _ \| |       | |
 | |__  | |__) | |__  | (___ | |__| | |   | |  | | | (___   __| |_ __   | |_) | |__   __| |
 |  __| |  _  /|  __|  \___ \|  __  | |   | |  | |  \___ \ / _` | '_ \  |  _ <| '_ \ / _` |
 | |    | | \ \| |____ ____) | |  | | |___| |__| |  ____) | (_| | | | | | |_) | | | | (_| |
 |_|    |_|  \_\______|_____/|_|  |_|\_____\____/  |_____/ \__,_|_| |_| |____/|_| |_|\__,_|
'''
# Choice for user to pick when starting the script
ScreenOne = '''
Select Your Choice
1. Login as Existing Customer
2. Register a New Account
3. Browse as Guest
4. Exit

'''
# Choices for MEMBERS to pick after login
ScreenTwo = '''
Select Your Choice
1. Browse All Products
2. Search Products by Keyword
3. My Profile
4. Main Menu
5. Exit

'''
# Choices for ADMIN to use after authorized
ScreenTwoAdmin = '''
Select Your Choice
1. Update Products
2. Search Products by Keyword
3. Check Orders
4. Search Orders by EMAIL
5. Main Menu
6. Exit

'''
# Choices for GUEST to use
ScreenTwoGuest = '''
Select Your Choice
1. Browse All Products
2. Search Products by Keyword
3. Main Menu
4. Exit

'''
# Choices for MEMBERS after S2 Complete to use
ScreenThreeMember = '''
Select Your Choice to be redirected to
1. Main Menu
2. Member's Selection Page
3. Exit

'''
# Choices for ADMIN after S2 Complete to use
ScreenThreeAdmin = '''
Select Your Choice to be redirected to
1. Main Menu
2. Admin's Selection Page
3. Exit

'''
# Choices for GUESTS after S2 Complete to use
ScreenThreeGuest = '''
Select Your Choice to be redirected to
1. Main Menu
2. Guest's Selection Page
3. Exit

'''
#Choices for MEMBERS after looking at products
ScreenThreeProductMEMBER = '''
Select Your Choice
1. Select and Place Order
2. Main Menu
3. Member's Selection Page
4. Exit

'''
#Choices for ADMINS after looking at products
ScreenThreeProductADMIN = '''
Select Your Choice
1. Add new product
2. Select and Edit product
3. Select and Remove product
4. Main Menu
5. Admin's Selection Page
6. Exit

'''

# Screen 1 Checking of choices made by user then redirecting to other dedicated functions
def S1ChoiceCheck():
    print(WELCOMENOTE)
    S1Choice = (input(ScreenOne))
    S1Choice = int(S1Choice)
    if S1Choice == 1:
        S1Choice1()
    elif S1Choice == 2:
        S1Choice2()
    elif S1Choice == 3:
        S1Choice3()
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()

# Choice 1 of Screen 1's Function | Login
def S1Choice1():
    USERNAME = input('Type in your Email Address: ')
    PASSWORD = input('Type in your Password: ')
    # Reading file
    loginfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/logindata.txt", "rt") 
    fullloginfiledata = loginfile.read()
    loginfile.close()
    loginfiledata = fullloginfiledata.split('\n')

    # Loop to check if EMAIl is stored, then check if email and pw matches
    for logindata in loginfiledata:
        if f'email: {USERNAME}' in fullloginfiledata:
            if f'email: {USERNAME}' in (logindata):
                if f'password: {PASSWORD}' in (logindata):
                    print('Login Success! You may now browse the store as a Member.')
                    time.sleep(1)
                    print(ClearPage)
                    print(WELCOMENOTE)
                    S2ChoiceCheckMember(USERNAME)
                else:
                    # Incorrect Password
                    print('Login Fail. Password does not match.')
                    print('Please try to Login again.')
                    time.sleep(3)
                    print(ClearPage)
                    S1ChoiceCheck()
            else:
                pass
        # Hard Saving ADMIN Login CREDENTIALS
        elif USERNAME == "admin@gmail.com":
            if PASSWORD == "admin@1234":
                print('Login Success! You may now browse and edit the store as an Admin.')
                time.sleep(1)
                print(ClearPage)
                print(WELCOMENOTE)
                S2ChoiceCheckAdmin()
            else:
                # Incorrect Password, Prevent any outsiders trying to breach in
                print('Login Fail. Password does not match.')
                print('Please try to Login again.')
                time.sleep(3)
                print(ClearPage)
                S1ChoiceCheck()
        else:
            # Email not registered or typo on email
            print('Login Fail. Email Address not registered on system.')
            print('Please try to Login again or Register a new account.')
            time.sleep(3)
            print(ClearPage)
            S1ChoiceCheck()

# Choice 2 of Screen 1's Function | Registration
def S1Choice2():
    USERNAME = input('Type in your Email Address: ')
    PASSWORD = input('Type in your Password: ')
    CONTACTNUMBER = input('Type in your Phone Number: ')
    ADDRESS = input('Type in your address (Please include Postcode & State): ')
    loginfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/logindata.txt", "r")
    fullloginfiledata = loginfile.read()
    loginfile.close()
    # Check if EMAIL is already registered, else register
    if f'email: {USERNAME}' in fullloginfiledata:
        print('Account associated with Email Address already exist. Please try to Login.')
        time.sleep(2)
        print(ClearPage)
        S1ChoiceCheck()
    else:
        loginfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/logindata.txt", "a")
        # The symbol "|"" is used between info because address most likely have ","
        registerform = f'email: {USERNAME}|password: {PASSWORD}|contactnumber: {CONTACTNUMBER}|address: {ADDRESS}\n'
        registerform = str(registerform)
        loginfile.write(registerform) # Adding the format of User Credentials into logindata.txt
        loginfile.close()
        print('Registration complete, you will be logged in and browsing the store as a Member.')
        time.sleep(1)
        print(ClearPage)
        print(WELCOMENOTE)
        # Run function of Member which is the general interface
        S2ChoiceCheckMember(USERNAME) 

# Choice 3 of Screen 1's Function | GUEST Mode
def S1Choice3():
    print('Browsing as Guest.')
    time.sleep(1)
    print(ClearPage)
    print(WELCOMENOTE)
    # Run function of Guest which is similar to general interface
    S2ChoiceCheckGuest()

# Screen2 Check on Choice made by user for Members
# USERNAME is needed so can search for profile and store info after order
def S2ChoiceCheckMember(USERNAME):
    S2Choice = int(input(ScreenTwo))
    if S2Choice == 1:
        print('Showing all product(s) available.')
        # Running function to show all products
        showallproducts(USERNAME)
    elif S2Choice == 2:
        keyword = input('Please type in your Keyword: ')
        print('Showing matching product(s) available')
        # Running function to show all products associated with keyword
        showfilterproduct(keyword, USERNAME)
    elif S2Choice == 3:
        print('Showing your profile.')
        loginfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/logindata.txt", "rt") 
        fullloginfiledata = loginfile.read()
        loginfile.close()
        loginfiledata = fullloginfiledata.split('\n')
        # Checking line by line for profile
        for logindata in loginfiledata:
            if f'email: {USERNAME}' in logindata:
                OrdersList = []
                orderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "rt") 
                fullorderfiledata = orderfile.read()
                orderfile.close()
                orderfiledata = fullorderfiledata.split('\n')
                for orderdata in orderfiledata:
                    formattedorder = orderdata.split(':')
                    if USERNAME in formattedorder[0]:
                        orderformatted = f'{formattedorder[1]} | {formattedorder[2]}'
                        OrdersList.append(orderformatted) # Append order that has the email associated
                DataEMAIL = logindata.split('|')[0].split(': ')[1]
                DataPASSWORD = logindata.split('|')[1].split(': ')[1]
                DataCONTACT = logindata.split('|')[2].split(': ')[1]
                DataADDRESS = logindata.split('|')[3].split(': ')[1]
                if OrdersList: # Checking if there's even any orders in the list
                    Orders = ("\n").join(OrdersList)
                    print(f'E-Mail: {DataEMAIL}\nPassword: {DataPASSWORD}\nContact Number: {DataCONTACT}\nAddress: {DataADDRESS}\nOrders:\n{Orders}\n')
                else:
                    print(f'E-Mail: {DataEMAIL}\nPassword: {DataPASSWORD}\nContact Number: {DataCONTACT}\nAddress: {DataADDRESS}\nOrders: Not Found\n')
        DONECheckMember(USERNAME)
    elif S2Choice == 4:
        # Returning to main menu
        print(ClearPage)
        S1ChoiceCheck()
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()

# Screen2 Check on Choice made by user for Admin
def S2ChoiceCheckAdmin():
    S2Choice = int(input(ScreenTwoAdmin))
    if S2Choice == 1:
        print('Showing all product(s) to be edited')
        # Running function to show all products
        showallproducts(USERNAME='ADMIN')
    elif S2Choice == 2:
        keyword = input('Please type in your Keyword: ')
        print('Showing matching product(s) to be edited')
        # Running function to show all products associated with keyword
        showfilterproduct(keyword, USERNAME='ADMIN')
    elif S2Choice == 3:
        # Fetch all orders stored in txt file
        print('Showing all Order(s)')
        orderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "rt") 
        fullorderfiledata = orderfile.read()
        orderfile.close()
        orderfiledata = fullorderfiledata.split('\n')
        if orderfiledata:
            print('-------------------------------------------------')
            print('Email Address', end=' \t| ')
            print('OrderID', end=' | ')
            print('Product', end='\t\t| ')
            print('')
            print('-------------------------------------------------')
            for orderdata in orderfiledata:
                OrderEMAIL =  orderdata.split(':')[0]
                OrderID =  orderdata.split(':')[1]
                OrderItem =  orderdata.split(':')[2]
                print(OrderEMAIL, end=' \t| ')
                print(OrderID, end=' | ')
                print(OrderItem,  end='\t\t| ')
                print('')
            print('-------------------------------------------------')
            DONECheckAdmin()
        else:
            print('No order(s) found.')
            DONECheckAdmin()

    # Filtering orders associated with emails
    elif S2Choice == 4:
        FilteredOrderList = []
        orderkeyword = input('Please type in EMAIL to find matching order(s): ')
        orderkeyword = orderkeyword.lower()
        orderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "rt") 
        fullorderfiledata = orderfile.read()
        orderfile.close()
        orderfiledata = fullorderfiledata.split('\n')
        for orderdata in orderfiledata:
            if orderkeyword in orderdata.split(':')[0]:
                FilteredOrderList.append(orderdata)
        # Check if any orders stored matching the email if not will not show any orders
        if FilteredOrderList:
            print('-------------------------------------------------')
            print('Email Address', end=' \t| ')
            print('OrderID', end=' | ')
            print('Product', end='\t\t| ')
            print('')
            print('-------------------------------------------------')
            for FilteredOrder in FilteredOrderList:
                OrderEMAIL =  FilteredOrder.split(':')[0]
                OrderID =  FilteredOrder.split(':')[1]
                OrderItem =  FilteredOrder.split(':')[2]
                print(OrderEMAIL, end=' \t| ')
                print(OrderID, end=' | ')
                print(OrderItem,  end='\t\t| ')
                print('')
            print('-------------------------------------------------')
            DONECheckAdmin()
        else:
            print('No matching order(s) to the EMAIL.')
            DONECheckAdmin()
    # Returning to main menu
    elif S2Choice == 5:
        print(ClearPage)
        S1ChoiceCheck()
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()
# Screen2 Check on Choice made by Guest User
def S2ChoiceCheckGuest():
    S2Choice = int(input(ScreenTwoGuest))
    if S2Choice == 1:
        showallproducts(USERNAME='GUEST')
    elif S2Choice == 2:
        keyword = input('Please type in your Keyword: ')
        showfilterproduct(keyword,USERNAME='GUEST')
    elif S2Choice == 3:
        print(ClearPage)
        S1ChoiceCheck()
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()
# Show filtered by keyword's products page after login/registration
def showfilterproduct(keyword,USERNAME):
    productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "rt")
    productsAll = productsfile.read()
    productsfile.close()
    AllProductList = productsAll.split(',')

    FilteredList = []
    for grocery in AllProductList:
        if keyword.lower() in grocery.split(':')[0].lower():
            FilteredList.append(grocery)
        else:
            pass
    # Check if any products matches with the keyword provided
    if FilteredList:
        print('-----------------------------------------------------------------')
        print('No ',end='|')
        print('Product', end='\t\t| ')
        print('Price', end=' | ')
        print('Amount', end='   \t| ')
        print('Origin', end='   \t|')
        print('')
        print('-----------------------------------------------------------------')
        counter = 1
        for filteredgrocery in FilteredList:
            PName =  filteredgrocery.split(':')[0]
            PPrice =  filteredgrocery.split(':')[1]
            PVolume =  filteredgrocery.split(':')[2]
            POrigin =  filteredgrocery.split(':')[3]
            print("%02d" % (counter), end=' |') # Make numbers like 1 to 01
            print(PName, end='\t\t| ')
            print(PPrice, end=' | ')
            print(PVolume, end='   \t| ')
            print(POrigin, end='   \t|')
            print('')
            counter+=1
        print('-----------------------------------------------------------------')
        if USERNAME == 'ADMIN':
            DONECheckAdmin()
        elif USERNAME == 'GUEST':
            DONECheckGuest()
        else:
            # Requesting for choice 
            STPMChoice = int(input(ScreenThreeProductMEMBER))
            # Placing order
            if STPMChoice == 1:
                SelectedProductNo = int(input('Please type in the "No." of the product you want to order: '))
                SelectedProductNo = SelectedProductNo - 1 # Because list count starts from 0
                # Try is used to check if the selected No. is in the item list
                try:
                    Item = FilteredList[SelectedProductNo]
                    # E.g. Item Banana:RM 06:1kg:Malaysia
                    ItemName = Item.split(':')[0]
                    ItemPrice = Item.split(':')[1]
                    print(f"\n{ItemName} for {ItemPrice}, successfully added to cart, proceeding confirm to your order.\n")
                    loginfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/logindata.txt", "rt") 
                    fullloginfiledata = loginfile.read()
                    loginfile.close()
                    loginfiledata = fullloginfiledata.split('\n')
                    for logindata in loginfiledata:
                        if f'email: {USERNAME}' in logindata:
                            DataCONTACT = logindata.split('|')[2].split(': ')[1]
                            DataADDRESS = logindata.split('|')[3].split(': ')[1]
                    print(f'\nOrder Details:\nProduct: {ItemName}\nPrice: {ItemPrice}\nEmail Address: {USERNAME}\nContact Number: {DataCONTACT}\nShipping Address: {DataADDRESS}')
                    ConfirmOrder = input('\nPlease type "YES" to confirm your order, anything else will cancel the order: ')
                    if ConfirmOrder.lower() == "yes":
                        print('\nConfirming Order, please wait a moment.')
                        orderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "rt")
                        readorderfile = orderfile.read()
                        orderfile.close()
                        orderfilelength = int(len(readorderfile.split('\n'))) + 1 # add 1 because current length is previous order number
                        print(orderfilelength)
                        ordernumber = ("%04d" % (orderfilelength)) # make numbers like 1 to 0001
                        writeorderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "a")
                        orderinfo = f'\n{USERNAME}:FRC{ordernumber}:{ItemName}'
                        writeorderfile.write(orderinfo)
                        writeorderfile.close()
                        print(f'Order Confirmed, Order Number: #FRC{ordernumber}, Email: {USERNAME}')
                        DONECheckMember(USERNAME)
                    else:
                        print('Order Not Placed...')
                        DONECheckMember(USERNAME)
                except:
                    print('Product "No." not found, please start over again.')
                    time.sleep(1)
                    DONECheckMember(USERNAME)
            elif STPMChoice == 2:
                print(ClearPage)
                S1ChoiceCheck()
            elif STPMChoice == 3:
                print(ClearPage)
                print(WELCOMENOTE)
                S2ChoiceCheckMember(USERNAME)
            else:
                # Exiting script
                print('Thanks for visiting FreshCO, see you again')
                time.sleep(2)
                exit()
    else:
        print('No product(s) matching the keyword found.')
        DONECheckMember(USERNAME)
# Show all products page after login/registration
def showallproducts(USERNAME):
    productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "rt")
    productsAll = productsfile.read()
    productsfile.close()
    AllProductList = productsAll.split(',')
    
    print('-----------------------------------------------------------------')
    print('No ',end='|')
    print('Product', end='\t\t| ')
    print('Price', end=' | ')
    print('Amount', end='   \t| ')
    print('Origin', end='   \t|')
    print('')
    print('-----------------------------------------------------------------')
    counter = 1
    for grocery in AllProductList:
        PName =  grocery.split(':')[0]
        PPrice =  grocery.split(':')[1]
        PVolume =  grocery.split(':')[2]
        POrigin =  grocery.split(':')[3]
        print("%02d" % (counter), end=' |')
        print(PName, end='\t\t| ')
        print(PPrice, end=' | ')
        print(PVolume, end='   \t| ')
        print(POrigin, end='   \t|')
        print('')
        counter+=1
    print('-----------------------------------------------------------------')
    if USERNAME == 'ADMIN':
        STPAChoice = int(input(ScreenThreeProductADMIN))

        if STPAChoice == 1:
            # Add new product
            productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "a")
            NewName = input("Enter the new product's Name: ")
            NewPrice = input("Enter the new product's Price: ")
            NewVol = input("Enter the new product's Volume: ")
            NewOrigin = input("Enter the new product's Origin: ")
            productsAddNew = productsfile.write(f',{NewName}:{NewPrice}:{NewVol}:{NewOrigin}')
            print("Product Added")
            productsfile.close()
            DONECheckAdmin()

        elif STPAChoice == 2:
            # Edit selected product
            SelectedProductNo = int(input('Type in the "No." of the product to Edit: '))
            SelectedProductNo = SelectedProductNo - 1
            try:
                Item = AllProductList[SelectedProductNo]
                ItemName = Item.split(':')[0]
                ItemPrice = Item.split(':')[1]
                ItemVolume = Item.split(':')[2]
                ItemOrigin = Item.split(':')[3]
                ItemUpdateChoice = int(input(f'Select what to be changed\n1. {ItemName}\n2. {ItemPrice}\n3. {ItemVolume}\n4. {ItemOrigin}\n'))
                # If and ELIF and ELSE statements so admin can pick what they want to edit
                if ItemUpdateChoice == 1:
                    NewName = input(f'Type in the New Name: ')
                    productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "w")
                    productsAllEdited = productsAll.replace(f'{Item}',f'{NewName}:{ItemPrice}:{ItemVolume}:{ItemOrigin}')
                    productsAll = productsfile.write(productsAllEdited)
                    productsfile.close()
                elif ItemUpdateChoice == 2:
                    NewPrice = input(f'Type in the New Price: ')
                    productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "w")
                    productsAllEdited = productsAll.replace(f'{Item}',f'{ItemName}:{NewPrice}:{ItemVolume}:{ItemOrigin}')
                    productsAll = productsfile.write(productsAllEdited)
                    productsfile.close()
                elif ItemUpdateChoice == 3:
                    NewVol = input(f'Type in the New Volume: ')
                    productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "w")
                    productsAllEdited = productsAll.replace(f'{Item}',f'{ItemName}:{ItemPrice}:{NewVol}:{ItemOrigin}')
                    productsAll = productsfile.write(productsAllEdited)
                    productsfile.close()
                else:
                    NewOrigin = input(f'Type in the New Origin: ')
                    productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "w")
                    productsAllEdited = productsAll.replace(f'{Item}',f'{ItemName}:{ItemPrice}:{ItemVolume}:{NewOrigin}')
                    productsAll = productsfile.write(productsAllEdited)
                    productsfile.close()
                print('Product Edited')
                DONECheckAdmin()
            except:
                print('Product "No." not found, please start over again.')
                time.sleep(1)
                DONECheckAdmin()

        elif STPAChoice == 3:
            # Remove selected product by replacing item with '' (empty)
            SelectedProductNo = int(input('Type in the "No." of the product to Remove: '))
            SelectedProductNo = SelectedProductNo - 1
            try:
                Item = AllProductList[SelectedProductNo]
                productsfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/products.txt", "w")
                productsAllEdited = productsAll.replace(f',{Item}','')
                productsAll = productsfile.write(productsAllEdited)
                productsfile.close()
                print('Product Removed')
                DONECheckAdmin()
            except:
                print('Product "No." not found, please start over again.')
                time.sleep(1)
                DONECheckAdmin()
        
        elif STPAChoice == 4:
            print(ClearPage)
            S1ChoiceCheck()
        
        elif STPAChoice == 5:
            print(ClearPage)
            print(WELCOMENOTE)
            S2ChoiceCheckAdmin()
        
        else:
            # Exiting script    
                
            time.sleep(2)
            exit()
    elif USERNAME == 'GUEST':
        DONECheckGuest()
    else:
        # Members part to make order
        STPMChoice = int(input(ScreenThreeProductMEMBER))
        if STPMChoice == 1:
            SelectedProductNo = int(input('Please type in the "No." of the product you want to order: '))
            SelectedProductNo = SelectedProductNo - 1
            try:
                Item = AllProductList[SelectedProductNo]
                ItemName = Item.split(':')[0]
                ItemPrice = Item.split(':')[1]
                print(f"\n{ItemName} for {ItemPrice}, successfully added to cart, proceeding confirm to your order.\n")
                loginfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/logindata.txt", "rt") 
                fullloginfiledata = loginfile.read()
                loginfile.close()
                loginfiledata = fullloginfiledata.split('\n')
                # Get other MEMBER data to show before confirming order
                for logindata in loginfiledata:
                    if f'email: {USERNAME}' in logindata:
                        DataCONTACT = logindata.split('|')[2].split(': ')[1]
                        DataADDRESS = logindata.split('|')[3].split(': ')[1]
                print(f'\nOrder Details:\nProduct: {ItemName}\nPrice: {ItemPrice}\nEmail Address: {USERNAME}\nContact Number: {DataCONTACT}\nShipping Address: {DataADDRESS}')
                ConfirmOrder = input('Please type "YES" to confirm your order, anything else will cancel the order: ')
                # Check if user confirms to order
                if ConfirmOrder.lower() == "yes":
                    print('\nConfirming Order, please wait a moment.')
                    orderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "rt")
                    readorderfile = orderfile.read()
                    orderfile.close()
                    orderfilelength = int(len(readorderfile.split('\n')))
                    ordernumber = ("%04d" % (orderfilelength))
                    writeorderfile = open("C:/Users/Lucas/Desktop/Degree Year 1/Degree Y1S1/PYP_ASSIGNMENT/orders.txt", "a")
                    orderinfo = f'\n{USERNAME}:FRC{ordernumber}:{ItemName}'
                    writeorderfile.write(orderinfo)
                    writeorderfile.close()
                    print(f'Order Confirmed, Order Number: #FRC{ordernumber}, Email: {USERNAME}')
                    DONECheckMember(USERNAME)
                else:
                    print('Order Not Placed...')
                    DONECheckMember(USERNAME)
            except:
                print('Product "No." not found, please start over again.')
                time.sleep(1)
                DONECheckMember(USERNAME)
        elif STPMChoice == 2:
            print(ClearPage)
            S1ChoiceCheck()
        elif STPMChoice == 3:
            print(ClearPage)
            print(WELCOMENOTE)
            S2ChoiceCheckMember(USERNAME)
        else:
            # Exiting script
            print('Thanks for visiting FreshCO, see you again')
            time.sleep(2)
            exit()

def DONECheckMember(USERNAME):
    # Let USER Pause and confirm they are done before directing to another page
    input('Press ENTER once done.')
    print(ClearPage)
    print(WELCOMENOTE)
    DONECHOICE = int(input(ScreenThreeMember))
    if DONECHOICE == 1:
        print(ClearPage)
        S1ChoiceCheck()
    elif DONECHOICE == 2:
        print(ClearPage)
        print(WELCOMENOTE)
        S2ChoiceCheckMember(USERNAME)
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()

def DONECheckAdmin():
    # Let USER Pause and confirm they are done before directing to another page
    input('Press ENTER once done.')
    print(ClearPage)
    print(WELCOMENOTE)
    DONECHOICE = int(input(ScreenThreeAdmin))
    if DONECHOICE == 1:
        print(ClearPage)
        S1ChoiceCheck()
    elif DONECHOICE == 2:
        print(ClearPage)
        print(WELCOMENOTE)
        S2ChoiceCheckAdmin()
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()

def DONECheckGuest():
    # Let USER Pause and confirm they are done before directing to another page
    input('Press ENTER once done.')
    print(ClearPage)
    print(WELCOMENOTE)
    DONECHOICE = int(input(ScreenThreeGuest))
    if DONECHOICE == 1:
        print(ClearPage)
        S1ChoiceCheck()
    elif DONECHOICE == 2:
        print(ClearPage)
        print(WELCOMENOTE)
        S2ChoiceCheckGuest()
    else:
        # Exiting script
        print('Thanks for visiting FreshCO, see you again')
        time.sleep(2)
        exit()

S1ChoiceCheck()