import random

def load_word_list(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def provide_feedback(word, guess):
    feedback = ""
    for i in range(len(word)):
        if word.lower().find(guess[i].lower()) == -1:
            feedback += "-"
        elif word.lower().find(guess[i].lower()) != -1:
            if word[i] == guess[i]:
                feedback += word[i]
            else:
                feedback += "+"
    return feedback

def main():
    word_list = load_word_list("valid-wordle-words.1.txt")
    word = random.choice(word_list)

    replacing_plus = "+"  # letter is in the word, but wrong position
    replacing_minus = "-"  # letter not in word

    print("You play by guessing different five-letter words to see how close they are to the secret word.")
    print("When you submit a guess, the game will tell you how close your guess is by printing a '+' or '-' for each letter.")
    print("'+' means that your letter is in the word, but in the wrong location.")
    print("'-' means this letter is not included in the word. Hope you have fun!")
    print("type 'stop' to quit the game\n")

    guess = input("What's your guess: ")

    while guess.lower() != word.lower():
        if guess.lower() == 'stop':
            print(f"Better luck next time! The word was: {word}")
            break
        elif len(guess) != len(word):
            print("Wrong length! Guess again")
        elif guess.lower() not in [w.lower() for w in word_list]:
            print("Not a valid word! Guess again")
        else:
            feedback = provide_feedback(word, guess)
            print(feedback)
            print("Guess again")

        guess = input()

    if guess.lower() == word.lower():
        print(f"Congrats, {word} is the answer!")

if __name__ == "__main__":
    main()