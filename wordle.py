import sys

# Line above gets the today's word from command line.
WoD = (sys.argv[1])

# Variables have been assigned to certain numbers to tell the user about which letter is correct, how many tries they have and how many times they took a guess.
triesLeft = 6  # given tries for user
attempt = 0  # how many attempts user made
letter = 0  # which letters are being compared

# If given input for today's word is correct, instructions will be shown.
if len(WoD) == 5 and WoD == WoD.upper():
    print("Welcome to the game Wordle. RULES:\n"
          "You have 6 tries to guess the today's word.\n"
          "Your guess must be in all uppercase letters.\n"
          "If you want to leave, press B. ")

while triesLeft > 0:
    # If given input has more or less characters than 5, the game will give an error and player must give an input again.
    if len(WoD) != 5:
        print("ERROR: The word given can not contain less or more than 5 letters. Please give a different input.")
        break

    if WoD != WoD.upper():
        print("ERROR: The word given can not contain lowercase letters. Please write your word in uppercase letters.")
        break

    guessWord = str(input(f"Take a guess! You have {triesLeft} tries left. : "))

    if guessWord != guessWord.upper() and guessWord != "b":
        print("ERROR: The word given can not contain lowercase letters. Please write your word in uppercase letters.")

    if guessWord == "B" or guessWord == "b":
        print("Leaving the game...")
        break

    attempt += 1
    # If player guesses the correct word, the code will say in which try player guessed the right word, with the correct suffixes, then game will end.
    if guessWord.strip() == WoD:
        if attempt == 1:
            suffix = "st"
        elif attempt == 2:
            suffix = "nd"
        elif attempt == 3:
            suffix = "rd"
        elif attempt > 3:
            suffix = "th"
        print(f"Congratulations! You have guessed the correct word in {attempt}{suffix} try.")
        break

    # If given word has more or less characters than 5, the game will give a warning and no tries will be consumed.
    elif len(guessWord.strip()) != 5:
        print("WARNING: You must write a word that contains 5 letters.")
        attempt -= 1

    # If player doesn't guess the right word, a for loop starts comparing each index for given word and WoD.
    elif len(guessWord.strip()) == 5 and guessWord == guessWord.upper():
        triesLeft -= 1

        for indexGuess, indexWord in zip(guessWord.strip(),
                                         WoD):  # zip function matches de indexes of the words and compares them.
            letter += 1  # after each index, letter variable increases by 1, so player will know each letter's place.
            if indexGuess in WoD and indexGuess == indexWord:
                print(f"{letter}. letter exists and located in right position.")

            elif indexGuess in WoD and indexGuess != indexWord:
                print(f"{letter}. letter exists but located in the wrong position.")

            else:
                print(f"{letter}. letter does not exist.")
    letter = 0  # after a for loop, letter variable resets so in the next try, it will start from 1 again.

# If user uses all of their tries, game ends.
if triesLeft == 0:
    print("You're failed!")
