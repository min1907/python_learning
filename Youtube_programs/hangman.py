import random
from Youtube_programs.words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while "-" in word or " " in words:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(
            "You have ",
            lives,
            "lives left and you have used these letters: ",
            " ".join(used_letters),
        )

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives -= 1  # take away a live is it's wrong
                print("\nYour letter", user_letter, "is not in the word")
        elif user_letter in used_letters:
            print("you have already used that character. Please try again.")
        else:
            print("Invalid character")

    # gets here when len(word_letters) == 0
    if lives == 0:
        print("You died, sorry, the word is: ", word)
    else:
        print("Yay! You guessed the word ", word, "!!")


if __name__ == "__main__":
    hangman()
