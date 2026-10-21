import random
import time

art = {
    "rock": r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

    "paper": r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

    "scissors": r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

name = input("What is your name? ").strip()

playingpreference = input(
    f"Hello, {name}! Welcome to Rock, Paper, Scissors. Would you like to hear the rules? (y/n): "
).strip().lower()

if playingpreference in ["y", "yes"]:
    print("\nRules:")
    print(" Rock beats Scissors")
    print(" Scissors beats Paper")
    print(" Paper beats Rock")
    print(" First to 3 points wins\n")

ready = input("Ready to begin? (y/n): ").strip().lower()

if ready == "y":

    player_score = 0
    computer_score = 0
    round_num = 1

    while player_score < 3 and computer_score < 3:

        print(f"\n========== ROUND {round_num} ==========")

        player = input(
            "Choose rock, paper, or scissors: "
        ).strip().lower()

        if player not in ["rock", "paper", "scissors"]:
            print("Invalid choice!")
            continue

        computer = random.choice(["rock", "paper", "scissors"])

        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("SHOOT!\n")

        print(f"{name} chose:")
        print(art[player])

        print("Computer chose:")
        print(art[computer])

        if player == computer:
            print(":| Draw!")

        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print(":D You win this round!")
            player_score += 1

        else:
            print(":( Computer wins this round!")
            computer_score += 1

        print(f"\nScore:")
        print(f"{name}: {player_score}")
        print(f"Computer: {computer_score}")

        round_num += 1

    print("\n========== GAME OVER ==========")

    if player_score > computer_score:
        print(f":D Congratulations {name}, you win!")
    else:
        print(":( The computer wins!")

else:
    print("Maybe another time!")