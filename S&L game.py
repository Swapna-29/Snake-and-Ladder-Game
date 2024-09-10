import random

# Initialize board, snakes, and ladders
board_size = 100
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(position, roll):
    position += roll
    if position > board_size:
        position = board_size - (position - board_size)
    return position

def check_snake_ladder(position):
    if position in snakes:
        print(f"Oops! Bitten by a snake. Sliding down from {position} to {snakes[position]}")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder from {position} to {ladders[position]}")
        return ladders[position]
    return position

def play_game():
    player_position = 0
    while player_position < board_size:
        input("Press Enter to roll the dice...")
        roll = roll_dice()
        print(f"Rolled a {roll}")
        player_position = move_player(player_position, roll)
        player_position = check_snake_ladder(player_position)
        print(f"Player is now at position {player_position}")
        if player_position == board_size:
            print("Congratulations! You've won the game!")
            break

# Start the game
play_game()
