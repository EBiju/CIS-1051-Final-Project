#Code was based on this video  https://www.youtube.com/watch?v=m4nEnsavl6w
import random

from words import word_list
def find_words():
    chosenword = random.choice(word_list)
    return chosenword.upper()

def play(chosenword):
    word_completion = "_" * len(chosenword)
    guessed = False
    guessed_letters =[]
    guessed_words = []
    tries = 7

    print("Yo let's play hangman!")
    print(display_body(tries))
    print("\n")
    while not guessed and tries > 0:
        userguess = input("Please guess a letter or word: ").upper()
        if len(userguess) == 1 and userguess.isalpha():
            if userguess in guessed_letters:
                print("You already guessed the letter/word", userguess)
            elif userguess not in chosenword:
                print(userguess, "is not in the word.")
                tries -= 1
                guessed_letters.append(userguess)
            else:
                print("Good job,", userguess, "is a letter the word!")
                guessed_letters.append(userguess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(chosenword) if letter == userguess]
                for index in indices:
                    word_as_list[index] = userguess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(userguess) == len(chosenword) and userguess.isalpha():
            if userguess in guessed_words:
                print("You already guessed that letter/word.", userguess)
            elif userguess != chosenword:
                print(userguess, "is not a letter in the word.")
                tries -= 1
                guessed_words.append(userguess)
                
            else:
                guessed = True
                word_completion = chosenword

        else:
            print("Not a valid guess")
        print(display_body(tries)) 
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guesed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + chosenword + ". Better luck next time!") 

#del-elif x == 22 and y == 33, return y = 22 and x == 33
#elif y == 22 and x == 32, x == 22, y == 29, x == 35
#identify

def display_body(tries):
    stages = [
            """
               ------------
                |         |
                |         O
                |        \|/
                |         |
                |        / \\
            -----
            """
            ,
              """
                ------------
                |          |
                |          O
                |         \|/
                |          |
                |           \\
            -----
              """
            ,
              """
                ------------
                |          |
                |          O
                |         \\|/
                |          |
                |         
            -----
              """
            ,
              """
                ------------
                |          |
                |          O
                |         \\|/
                |          
                |         
            -----
              """
            ,
            """
                ------------
                |          |
                |          O
                |         \\|
                |          
                |         
            -----
            """
            ,
            """
                ------------
                |          |
                |          O
                |          |
                |          
                |         
            -----
            """
            ,
            """
                ------------
                |          |
                |          O
                |          
                |          
                |         
            -----
            """
             ,
              """
                ------------
                |          |
                |          
                |           
                |          
                |         
            -----
            """
            
    ]
    return stages[tries]

def main():
    chosenword = find_words()
    play(chosenword)
    while input("Play again? (Y/N)").upper() == "Y":
        chosenword = find_words()
        play(chosenword)


#As int of x == 21, delete 3 for x == 12

if __name__ == "__main__":
    main()

