import string

remaining_attempts = 5

answer = input("Enter your phrase: ").upper()
answer = list(answer)
print("\n"*10) # I couldn't figure out how to clear the screen in the terminal, so this will have to do...

hidden_answer = ["_"] * len(answer)

for iteration, char in enumerate(answer):
    if char == " ":
        hidden_answer[iteration] = " "

chars = string.ascii_uppercase
chars = list(chars)
remaining_chars = chars.copy()

def divider():
    print("____________________________________________________________________________________________________________________________________________________")

def ascii_art():
    if remaining_attempts == 0:
        print("    _M_   ")
        print("     O    ")
        print("   --|--  ")
        print("     ^    ")
        print("    | |   ")
    elif remaining_attempts == 1:
        print("    _M_   ")
        print("     O    ")
        print("   --|--  ")
        print("     ^    ")
    elif remaining_attempts == 2:
        print("    _M_   ")
        print("     O    ")
        print("   --|--  ")
    elif remaining_attempts == 3:
        print("    _M_   ")
        print("     O    ")
    elif remaining_attempts == 4:
        print("    _M_   ")
    else:
        pass

def game():
    divider()

    global remaining_attempts

    guess = input("Choose a letter: ").upper()
    if guess == ''.join(answer):
        divider()
        print("You've guessed the complete phrase!")
        print("Congratulations! You Win!")
        divider()
        input("Press any key to exit...")
        exit()
    elif guess not in remaining_chars:
        pass
    else:
        remaining_chars.remove(guess)

    if guess not in (chars or [" "]):
        print("Invalid Input")
        input("Press Enter to try again... ")
        game()
    elif guess not in answer:
        print(guess + " is not part of the phrase...")
        remaining_attempts -= 1
    elif guess in answer:
        print(guess + " is part of the phrase!")
        for i, char in enumerate(answer):
            if char == guess:
                hidden_answer[i] = guess
    else:
        print("ERROR: Invalid Input")

while True:
    divider()
    ascii_art()
    print(f"Remaining Letters: {', '.join(remaining_chars)}")
    print(f"Answer: {' '.join(hidden_answer)}")
    if hidden_answer == answer:
        divider()
        print("You've guessed the complete phrase!")
        print("Congratulations! You Win!")
        divider()
        input("Press any key to exit...")
        break
    elif remaining_attempts != 0:
        game()
        print(f"You have {remaining_attempts} more tries")
    else:
        break