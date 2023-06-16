#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    item_menu = {"item1": ["Biscuits", 5, 20.50], 'item2': ['Cereals', 10, 90.00], 'item3': ['chicken', 20, 200.00],
                 'item4': ['Oats', 20, 39.99], 'item5': ['Rice', 30, 79.99]}
    cart = {}
    user_details = {}

    print("ESSENTIAL ITEMS AVAILABLE")
    print("%20s %20s %20s %20s" % ("S_no", 'Item', 'QTY', 'Cost'))
    print("%20s %20s %20s %20s" % ("1", 'Biscuits', '5', '20.50'))
    print("%20s %20s %20s %20s" % ("2", 'Cereal', '10', '90.00'))
    print("%20s %20s %20s %20s" % ("3", 'Chicken', '20', '200.00'))
    print("%20s %20s %20s %20s" % ("4", 'Oats', '20', '39.99'))
    print("%20s %20s %20s %20s" % ("5", 'Rice', '30', '79.99'))
 #   print(cart)

    def takeord(cart):
        print("How many biscuit packets are required? ")
        bis_qty = int(input(" Biscuit QTY "))
        cart.update({'Biscuits': bis_qty})

        print("How many cereal packets are required? ")
        crl_qty = int(input(" Cereal QTY "))
        cart.update({'Cereal': crl_qty})

        print("How many frozen chicken packets are required? ")
        fchk_qty = int(input(" frozen chicken QTY "))
        cart.update({'Chicken': fchk_qty})

        print("How many oats packets are required? ")
        ots_qty = int(input(" oats QTY "))
        cart.update({'Oats': ots_qty})

        print("How many rice packets are required? ")
        rc_qty = int(input(" rice QTY "))
        cart.update({'Rice': rc_qty})

    def user(user_details):
        print("Fill in your delivery details")

        print("Enter your name ")
        name = input("Name")
        user_details.update({'Name': name})

        print("Enter your address = ")
        address = input("Address = ")
        user_details.update({'Address': address})

        print("Distance from store ")
        dist = int(input("Distance in 5, 10 or 15km ONLY = "))
        user_details.update({'Distance': dist})

    def invoice(cart, user_details):
        print("Bill")
        print("%20s %20s %20s %20s" % ("S_no", 'Item', 'QTY', 'Total'))
        print("%20s %20s %20s %20s" % ("1", 'Biscuits', cart['Biscuits'], 20.5 * cart['Biscuits']))
        print("%20s %20s %20s %20s" % ("2", 'Cereal', cart['Cereal'], 90 * cart['Cereal']))
        print("%20s %20s %20s %20s" % ("3", 'Chicken', cart['Chicken'], 200 * cart['Chicken']))
        print("%20s %20s %20s %20s" % ("4", 'Oats', cart['Oats'], 39.99 * cart['Oats']))
        print("%20s %20s %20s %20s" % ("5", 'Rice', cart['Rice'], 79.99 * cart['Rice']))

        #  print("Total amount to be paid = ", (20.5 * cart['Biscuits']) + (90 * cart['Cereal']) + (200 * cart['Chicken']) + (39.99 * cart['Oats']) + (79.99 * cart['Rice']))
        print("")
        print()
        tot = (20.5 * cart['Biscuits']) + (90 * cart['Cereal']) + (200 * cart['Chicken']) + (39.99 * cart['Oats']) + (
                    79.99 * cart['Rice'])
        print("Based on your distance, the delivery charge will be ", 2 * user_details['Distance'])
        divchar = 2 * user_details['Distance']
        print("Total Bill amount = ", tot + divchar)

    def invenupdate(item_menu):
        item_menu['item1'][1] = item_menu['item1'][1] - cart['Biscuits']
        item_menu['item2'][1] = item_menu['item2'][1] - cart['Cereal']
        item_menu['item3'][1] -= cart['Chicken']
        item_menu['item4'][1] -= cart['Oats']
        item_menu['item5'][1] -= cart['Rice']

    takeord(cart)
    user(user_details)
    invoice(cart, user_details)
    

    if(input("Do you want to continue? y/n").lower() == 'y'):
        main()
    else:
        print("Have a nice day!!")

main()

