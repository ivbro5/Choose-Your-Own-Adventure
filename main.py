print("               Game loading... Please wait.")
print(" ")
print(" ")
print("\033[35m","     ☆ Welcome to Choose Your Own Adventure Game! ☆","\033[0m")
print(" ")
name = input("Enter your name, traveler: ")
print(" ")
print("Nice to meet you", name + ", choose one of the three elements to start off.")
#
print(" ")
print("\033[31m","0 - Pyro: Fire element","\033[0m")
print("\033[34m","1 - Hydro: Water element","\033[0m")
print("\033[36m","2 - Cryo: Ice element","\033[0m")
print(" ")

choice1 = int(input("Enter your choice here (0, 1, 2): "))

if choice1 == 0:
  print("You chose Pyro!")
elif choice1 == 1:
  print("You chose Hydro!")
elif choice1 == 2:
  print("You chose Cryo!")
else:
  print("Invalid choice. Try again.")
  exit()
print("  ")
#
print("  ")
print("Now, choose a weapon to equip for your journey.")
print(" ")
print("\033[30m","0 - Baseball bat","\033[0m")
print("\033[33m","1 - Bow & Arrow","\033[0m")
print("\033[35m","2 - Dual Swords","\033[0m")
print(" ")

choice2 = int(input("Enter your choice here (0, 1, 2): "))

if choice2 == 0:
  print("You chose Baseball bat! Batter up!")
elif choice2 == 1:
  print("You chose Bow & Arrow! Your aim must be great.")
elif choice2 == 2:
  print("You chose Dual Sword! Better to have two than one.")
else:
  print("Invalid choice. Try again.")
  exit()
  
#
print(" ")
print("Now, before you set off to begin your journey you need to beat an enemy first to test your strength. Your current health is 100. Pick an enemy to battle.")
print(" ")
print("\033[32m","0 - Goblin: Health = 30","\033[0m")
print("\033[33m","1 - Pirate: Health = 80","\033[0m")
print("\033[31m","2 - Knight: Health = 150","\033[0m")
print(" ")
choice3 = int(input("Enter your choice here (0, 1, 2): "))
print(" ")

if choice3 == 1:
  print("Was a close call, but you single-handedly defeated the Pirate! Your current health is 20. Find some food fast to heal up. Good luck on your journey", name + "!")
elif choice3 == 2:
  print("Oh no! The knight has finished you off. Game over, try again!")
elif choice3 == 0:
  print("That was easy! Your current health is 70. Find some food to restore it. Good luck on your journey", name + "!")
else:
  print("Invalid choice. Try again.")
  exit()