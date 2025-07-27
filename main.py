import random

while True:
  num_dice_input = input("How many dice do you want to roll? (or type 'exit' to quit): ").lower()
  if num_dice_input == "exit":
    print("Good Bye!")
    break

  try:
    num_dice = int(num_dice_input)
    if num_dice <= 0:
      print("Please enter a positive number of dice.")
      continue
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  results = []
  for _ in range(num_dice):
    results.append(random.randint(1, 6))

  print(f'You rolled: {tuple(results)}')

  while True:
    roll_again_choice = input("Roll again with the same number of dice? (yes/no OR y/n or exit): ").lower() # Added exit option
    if roll_again_choice in ["yes", "y"]:
      break
    elif roll_again_choice in ["no", "n"]:
      print("Thanks for playing!")
      break # Changed exit() to break
    elif roll_again_choice == "exit": # Handle exit in the inner loop
      print("Good Bye!")
      exit() # Still exit the program when typing exit
    else:
      print("Invalid choice. Please enter 'yes' or 'no'.")
