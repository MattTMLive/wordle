import random
import json

def get_word():
    with open("words.json") as words:
        words = json.load(words)

    word = words[random.randint(0, len(words))]
    #word = "balls"
    return word

def make_a_guess(guess, word):
    output = ""
    for num, letter in enumerate(list(guess)):
        if letter == word[num]: # If letter is correct
            output += letter.upper()
        elif letter in list(word):
            output += letter.lower()
        else:
            output += "_"
    return output

def main_game():
    turns = 0
    word = get_word()
    print("Turn 1")
    for turns in range(0, 6):
        print("Make a guess: ", end="")
        output = make_a_guess(input(), word)
        print(output, end="\n\n")
        if turns+2 == 7:
            print(f"You lost!! The word was {word}")
            break
        elif "_" in list(output):
            print(f"Turn {turns+2}")
        else:
            print(f"Genius, the word was {word}!")
            break
        turns += 1


# Main code
main_game()
