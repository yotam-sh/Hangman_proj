import random

word, player_input, join_string, menu_input = '', '', '', ''
lost, won = 0, 0
word_list = ['python', 'java', 'swift', 'javascript']
new_word, letter_list, hint, tried_letters = [], [], [], []
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '"', "'",
                 ';', ':', '/', '?', '.', '>', ',', '<', '\\', ']', '[', '{',
                 '}', '+', '=', '-', '_', '`', '~']


def main_menu():
    global menu_input
    print('H A N G M A N')
    menu_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    return menu_input


def randomizer():
    global word, letter_list, hint, new_word
    word = random.choice(word_list)
    [(new_word.append(letter)) for letter in word]
    letter_list = []
    hint = "-" * len(word)
    return player_input, word, hint


def move_checker():
    global player_input, letter_list, hint, new_word, join_string, tried_letters, lost, won
    tries = 8

    while tries > 0:
        print('\n' + hint)
        player_input = input('Input a letter: ')

        # Check if input is a single letter and if input is in alphabet and if input is in chosen word
        if len(player_input) == 1 and 'a' <= player_input <= 'z' and player_input in new_word:

            # Checks if input was already guessed
            if player_input in hint:
                print("You've already guessed this letter.")
            else:
                counter = 0
                for i, j in zip(new_word, hint):

                    # Compares the chosen word to state of guesses and inserts correct guesses
                    if i == player_input and j == '-':
                        temp = [i for i in hint]
                        temp[counter] = player_input
                        hint = "".join(temp)
                    counter += 1

        else:
            if len(player_input) != 1:
                print('Please, input a single letter.')
            elif 'A' <= player_input <= 'Z' or player_input in special_chars or player_input.isalpha() is False:
                print('Please, enter a lowercase letter from the English alphabet.')
            elif player_input not in new_word:
                if player_input in tried_letters:
                    print("You've already guessed this letter.")
                else:
                    print("That letter doesn't appear in the word.")
                    tried_letters.append(player_input)
                    tries -= 1

        # Checks if chosen word was completed and ends the game if True
        if "-" not in hint:
            print(f'You guessed the word {hint}!' + '\n' + 'You survived!')
            new_word, letter_list, hint, tried_letters = [], [], [], []
            won += 1
            break

    # Checks if player runs out of guesses
    if tries == 0:
        print('\n' + 'You lost!')
        new_word, letter_list, hint, tried_letters = [], [], [], []
        lost += 1


while menu_input != 'exit':
    main_menu()
    if menu_input == 'play':
        randomizer(), move_checker()
    elif menu_input == 'results':
        print(f'You won: {won} times' + '\n' + f'You lost: {lost} times')
    elif menu_input == 'exit':
        break
    else:
        continue

