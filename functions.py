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
      option4()
      
    elif selection == "5":
      print("Exit")
      loop = False

  print("Goodbye")
# end main()

def getMenuSelection():
  print("\nMAIN MENU")
  print("1: Option 1")
  print("2: Option 2")
  print("3: Option 3")
  print("4: Option 4")
  print("5: Exit")
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
  

  add_to_cart(new_item, new_price, amount)
    

def option3():
  old_item = input("\nPlease type the item you wish to remove: ").lower()
  old_price = int(input("\nPlease type the price of the item you wish to remove: $"))
  amount = int(input("\nHow many of that item would you like to remove: "))
  
  remove_from_cart(old_item, old_price, amount)

def option4():
  print("\nYour total price is: ")
  total = 0
  num_items = 0
  for items in shopping_list:
    total += items[1] * items[2]
    num_items += items[2]
  print("")
  print(total)
  print("\nyour total number of items is: " + str(num_items))

      

def add_to_cart(item, price, amount):

  for items in shopping_list:
    if items[0] == item and items[1] == price:
      items[2] += amount 
      return

  shopping_list.append([item, price, amount])

def remove_from_cart(item, price, amount):

  for items in shopping_list:
    if items[0] == item and items[1] == price and items[2] > amount:
      items[2] -= amount 
      return
    elif items[0] == item and items[1] == price and items[2] <= amount:
      shopping_list.remove(items)
      



