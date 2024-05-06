from Words import words
import random
import string

size = len(words)

def getValidWord(words) :
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = getValidWord(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    hangmanLimbs = 0

    while(len(word_letters) > 0) :
        print("You have used these letters:", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("".join(word_list))

        letter = input("Guess a letter: ").upper()
        if(letter in alphabet - used_letters):
            used_letters.add(letter)
            if(letter in word_letters):
                word_letters.remove(letter)
            else:
                hangmanLimbs += 1
        elif letter in used_letters:
            print("Already picked that letter")
        if hangmanLimbs >= 6:
            print(f"You lose! The word was {word}")
            return
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print("You win! The word was ", "".join(word_list))

if __name__ == "__main__":
    hangman()
