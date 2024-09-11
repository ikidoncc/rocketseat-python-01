_DATABASE = []

def CreateContact():
  print("\n...New contact...\n")

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
  ShowOptions()

  option_selected = int(input("\nPlease, enter a number: "))

  if(option_selected == 1): CreateContact()

  print(_DATABASE)


Main()