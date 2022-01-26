import random
import json

def get_word():
    with open("words.json") as words:
        words = json.load(words)

    word = words[random.randint(0, len(words))]
    #word = "added"
    return word

def make_a_guess(guess, word):
    output = ['_', '_', '_', '_', '_']
    words = list(word)

    for num, x in enumerate(range(0, 5)):
        if guess[num].lower() in words:
            output[num] = guess[num].lower()
            words.remove(guess[num])
        
        if guess[num].lower() == word[num]:
            if word[num].lower() in output:
                if word.count(word[num]) == 1:
                    output[output.index(word[num])] = "_"
            output[num] = word[num].upper()
            
        
        

        print("".join(output))
    
    return "".join(output)

def input_guess():
    the_input = ""
    while the_input == "":
        the_input = input("Make a guess: ").lower()
        if len(the_input) != 5:
            print("You did not enter a five letter word.")
            the_input = ""
    return the_input

def main_game():
    turns = 0
    word = get_word()
    for turns in range(0, 6):
        print(f"Turn {turns+1}")
        inputguess = input_guess()
        output = make_a_guess(inputguess, word)
        print(output, end="\n\n")    
        if inputguess != word:
            pass
        else:
            print(f"Genius, the word was {word}!")
            break
        if turns+1 == 6:
            print(f"You lost!! The word was {word}")
            break
        turns += 1


# Main code
main_game()
