import random

while True:
    print("Enter 'Exit' to quit")
    #Players
    player_1 = input("Please enter your name: ")
    player_2 = "AI"

    if player_1.title() == 'Exit':
        quit()

    #Game on!
    player_1_choice = input("Choose between r, p, or s for Rock, Paper or Scissors: ")
    print("--------------------------------------")
    print("Game on!")
    print(f"Player 1: {player_1}")
    print(f"Player 2: {player_2}")
    print("--------------------------------------")
    print(f"Your Choice: {player_1_choice}")

    #IA Choice
    ai_choices = ["r", "p", "s"]
    ai_choice = random.choice(ai_choices)

    print(f"{player_2} Choice: {ai_choice}")
    print("--------------------------------------")

    #Game Logic
    if player_1_choice.lower() == "r":
      if ai_choice == "p":
        print("You Lost")
      elif ai_choice == "s":
        print("Yayy You won!!!")
      elif ai_choice == "r":
        print("Draw")
        
    elif player_1_choice.lower() == "p":
      if ai_choice == "p":
        print("Draw")
      elif ai_choice == "s":
        print("You Lost")
      elif ai_choice == "r":
        print("Yayy You won!!!")
        
    elif player_1_choice.lower() == "s":
      if ai_choice == "p":
        print("Yayy You won!!!")
      elif ai_choice == "s":
        print("Draw")
      elif ai_choice == "r":
        print("You Lost")
        
    else:
      print("Please choose between r, p and s")
