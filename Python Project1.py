#Firstly we Define all the Functions that we'll need for
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
#We need to display all of the questions within in our Dictionary of questions that's why we use For loop
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT-(+5)!")
        return 1
    else:
        print("WRONG(0)!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------

#Created a Dictionary Named as "Questions"
questions = {
 "Guido van Rossum created Python?: ": "A",
 "Mexico City is largest Spanish-speaking city in the world?: ": "B",
 "The atomic number for lithium is 17?: ": "B",
 "Australia is wider than the moon?: ": "A",
 "There are 14 bones in a human foot?: ": "B"
}
#We have our own Questions but we will need some sort of collection to store our Amswers as option
#Then we created a List of List
options = [["A. TRUE", "B. FALSE"],
          ["A. False", "B. TRUE"],
          ["A. TRUE", "B. FALSE"],
          ["A. TRUE", "B. FALSE"],
          ["A. TRUE", "B. FALSE"]]
#Let's Generate a New Game Function as a New Game,to begin a new game
new_game()

while play_again():
    new_game()

print("Well Played!")
