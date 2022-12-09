import random
import string
from PIL import Image


def play_again():
    restart = input("Would you like to play again? y/n").lower()
    if restart == "y":
        play_game()
    elif restart == "n":
        print("k whatever...")


def play_game():
    with open('words.txt') as my_list:
        read_list = my_list.read()
    split_list = read_list.split()
    my_word = random.choice(split_list).upper()
    print(my_word)
    blanks = []
    wrong_guesses = []
    index = 0
    my_letters = [*my_word]

    for letter in my_letters:
        blanks.append('_')

    remaining_letters = [*string.ascii_uppercase]
    
    while len(wrong_guesses) < 8 and blanks != my_letters:
        print(f'\n{" ".join(blanks)}    Wrong Guesses: {" ".join(wrong_guesses)}\n')
        print(" ".join(remaining_letters))
        guess = input('guess a letter ').upper()
        while guess in remaining_letters: 
            remaining_letters.remove(guess)
        print(f'guess = {guess}')

        if len(guess) > 1 or not guess.isalpha():
            print(f"\nYa silly? 🤡 That's an invalid guess.")
        elif guess in blanks:
            print(f'\nYa silly? 🤡 You already guessed that!')
        elif guess in my_letters:
            for index, letter in enumerate(my_letters):
                if guess == letter:
                    blanks[index] = guess
            print(f'\nGreat job! 👍 \nGuesses Left: {8 - len(wrong_guesses)}')
        else:
            wrong_guesses.append(guess)
            print('\nNot this time! 👎 Try again? \nGuesses Left: '
                f'{8 - len(wrong_guesses)}')
        
    if wrong_guesses == 0:
        print(f'\nYou Lose! 🤬 \n{my_word}')
    else:
        print(f'Congratulations! You Won! 🚀 🏆 🥳')
    play_again()
        
        
        
        #image = Image.open("stone-cold-steve-austin.gif")
        #image.show()


if __name__ == "__main__":
    play_game()
