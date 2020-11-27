from shop_list import shopping_list 





def main():
  # Program Variables

  # Main Program Loop
  loop = True
  while loop:
    selection = getMenuSelection()

    if selection == "1":
      option1()
    elif selection == "2":
      option2()
    elif selection == "3":
      option3()
    elif selection == "4":
      print("Exit")
      loop = False

  print("Goodbye")
# end main()

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: Option 1")
  print("2: Option 2")
  print("3: Option 3")
  print("4: Exit")
  return input("Enter menu selection:")


def option1():
    print("\nShopping list-------------------------------------------------------")
    for items in shopping_list:
      print(items)
    print("----------------------------------------------------------------------")
      

def option2():
    new_item = input("\nPlease type the item you wish to add to the list: ").lower()
    new_price = int(input("\nPlease type the price of the item you wish to add: $"))
    amount = int(input("\nHow many of that item would you like: "))
    product = [new_item, new_price, amount]

    if shopping_list.count(product) == 0:
        shopping_list.append(product)
    elif shopping_list.count(product) >= 1:
        print("item is in list already")
        
        
       

def option3():
    print("\nYour total price is: ")
    total = 0
    num_items = 0
    for items in shopping_list:
        total += items[1] * items[2]
        num_items += items[2]
    print("")
    print(total)
    print("\nyour total number of items is: " + str(num_items))
# Call main to begin program
