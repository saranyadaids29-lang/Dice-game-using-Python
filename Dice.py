import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    player_score = 0
    computer_score = 0
    rounds = 5

    print("Dice Game: Player vs Computer\n")

    for i in range(1, rounds + 1):
        input(f"Press Enter to roll dice (Round {i})...")

        player = roll_dice()
        computer = roll_dice()

        print(f"You rolled: {player}")
        print(f"Computer rolled: {computer}")

        if player > computer:
            print("ou win this round!")
            player_score += 1
        elif player < computer:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {player_score} | Computer: {computer_score}\n")

    print("Final Result:")
    if player_score > computer_score:
        print(" You are the overall winner!")
    elif player_score < computer_score:
        print("Computer wins the game!")
    else:
        print(" It's a draw!")

play_game()
