from os import name, system

def clear_terminal():
    if name == "nt":
        system("cls")
    else:
        system("clear")

_DATABASE = [
  { "name": "ikidon", "phone": "999999999", "email": "ikidon@gmail.com", "favorite": 0 },
  { "name": "felipe", "phone": "111111111", "email": "felipe@gmail.com", "favorite": 1 }
  ]

def CreateContact():
  print("...New contact...\n")

  name = input("name: ")
  phone = input("phone: ")
  email = input("email: ")
  favorite = input("favorite (0 = No, 1 = Yes): ")

  contact = {
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite
    }

  _DATABASE.append(contact)

def ListAllContacts():
  print("...List all contacts...\n")

  for contact in _DATABASE:
    print(contact)

def UpdateContact():
  print("...Update a contact...\n")

  print("Yours contacts: ")
  for contact in _DATABASE:
    index = _DATABASE.index(contact)

    print(f"{index} - {contact.get("name")}")

  indexContact = int(input("\nWhich contact do you want to update? (Select by number on the right)\n> "))

  contact = _DATABASE[indexContact]

  print("\nLeave blank if you do not want to modify the current value.\n")
  name = input("name: ",)
  phone = input("phone: ")
  email = input("email: ")
  favorite = input("favorite (0 = No, 1 = Yes): ")

  if(len(name) > 0): contact.update({ "name": name })
  if(len(phone) > 0): contact.update({ "phone": phone })
  if(len(email) > 0): contact.update({ "email": email })
  if(favorite == 0 or favorite == 1): contact.update({ "favorite": favorite })

  _DATABASE[indexContact].update(contact)

def FavoriteOrUnfavorite():
  print("...Favorite or Unfavorite a contact...\n")
  
  print("Yours contacts: ")
  for contact in _DATABASE:
    index = _DATABASE.index(contact)

    print(f"{index} - {contact.get("name")}")

  indexContact = int(input("\nWhich contact do you want to update? (Select by number on the right)\n> "))

  favorite = input("favorite (0 = No, 1 = Yes): ")

  _DATABASE[indexContact].update({ "favorite": favorite})

#exclude
  print(_DATABASE)

def ListAllFavoriteContacts():
  print("...List all favorite contacts...\n")

  print("Yours favorite contacts:")
  for index in range(len(_DATABASE)):
    if(_DATABASE[index].get("favorite") == 1):
      print(f"{index} - {_DATABASE[index].get("name")}")

def DeleteContact():
  print("...Delete a contact...\n")

  print("Yours contacts: ")
  for contact in _DATABASE:
    index = _DATABASE.index(contact)

    print(f"{index} - {contact.get("name")}")

  indexContact = int(input("\nWhich contact do you want to update? (Select by number on the right)\n> "))

  _DATABASE.remove(_DATABASE[indexContact])

def ShowOptions():
  options = (
    "0. Welcome to agenda!",
    "1. Add a new contact",
    "2. List all contacts",
    "3. Edit a contact",
    "4. Favorite/Unfavorite a contact",
    "5. List all favorite contacts",
    "6. Delete a contact",
    "7. Exit"
    )
  
  for option in options:
    print(option)

def Main():
  clear_terminal()
  
  while True:
    print("\n-------MENU-------\n")
    ShowOptions()
    option_selected = int(input("\nPlease, enter a number: "))

    if(option_selected == 0):
      clear_terminal()
      
    elif(option_selected == 1): 
      clear_terminal()
      CreateContact()

    elif(option_selected == 2):
      clear_terminal()
      ListAllContacts()

    elif(option_selected == 3):
      clear_terminal()
      UpdateContact()

    elif(option_selected == 4):
      clear_terminal()
      FavoriteOrUnfavorite()

    elif(option_selected == 5):
      clear_terminal()
      ListAllFavoriteContacts()

    elif(option_selected == 6):
      clear_terminal()
      DeleteContact()

    elif(option_selected == 7): break

Main()