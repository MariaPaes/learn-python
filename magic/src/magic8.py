import random

def magic8():
    name = "Maria"
    question = " Is this real life?"
    answer = ""

    random_number = random.randint (1,9)
    print(random_number)

    if random_number == 1:
        answer = "Yes - definitely"
    elif random_number == 2:
        answer = "It is decidedly so"
    elif random_number == 3:
        answer = "Without a doubt"
    elif random_number == 4:
        answer = "Reply hazy, try again"
    elif random_number == 5:
        answer = "Ask again later"
    elif random_number == 6:
        answer = "Better not tell you now"
    elif random_number == 7:
        answer = "My sources say no"
    elif random_number == 8:
        answer = "Outlook not so good"
    elif random_number == 9:
        answer = "Very doubtful"
    else:
        answer =  "Error"

    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)


def conditionPlayAgain():
    playAgain = input("Would you like to play again? Answer with Y (to yes) or N (to no): ")
    if playAgain == "Y":
        magic8()
        conditionPlayAgain()
    elif playAgain == "N":
        print("See you on next time! Good time!")
    else:
        print("I don't understod. Repet!")
        playAgain = input("would you like to play again? Answer wiht Y (to yes) or N (to no): ")
        conditionPlayAgain()

magic8()
conditionPlayAgain()