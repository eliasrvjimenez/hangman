import random
import string

ALPHABET = string.ascii_lowercase


def generate_word():
    words_file = open("./words.txt", "r")
    words_raw = words_file.read()
    words = words_raw.split("\n")
    hidden_word = random.choice(words)
    return hidden_word


def play_game(word):
    lives = 7
    print("Welcome to Hangman! The word is %d letters long." % len(word))
    # print("debug word: %s" % word)
    player_word = '_' * len(word)
    correct_guesses = []
    while (lives > 0) and (player_word != word):
        print("You have %d lives left." % lives)
        print("Your current guess is: %s" % player_word)
        guess = input("Guess a letter:")
        if guess in ALPHABET and guess in word:
            correct_guesses += [guess]
            print("%s is in the word!" % guess)
            player_word = ''
            for i in range(0, len(word)):
                if word[i] in correct_guesses:
                    player_word += word[i]
                else:
                    player_word += '_'
            if player_word == word:
                print("You won!")
        elif guess in ALPHABET and guess not in word:
            print("Sorry, %s is not in the word." % guess)
            lives -= 1
        else:
            print("invalid character, please guess again")
    print("The word was %s." % word)


if __name__ == "__main__":
    play_game(generate_word())

