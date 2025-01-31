
import random


def MasterMind(guess_chance: int):
    comp_guess = str(random.randrange(1000, 10000))
    while (guess_chance > 0):
        user = input("enter the guess :")
        if (user == comp_guess):
            print("you are MasterMind !")
            break
        else:
            guess_chance -= 1
            print(f"{guess_chance} chances are left ")
            correct_guess = ['X']*4
            l = len(comp_guess)
            for i in range(l):
                if (user[i] == comp_guess[i]):
                    correct_guess[i] = user[i]
                elif user[i] in comp_guess:
                    print(f"{user[i]} is present in guess")

            print(correct_guess)
            if (user == ''.join(correct_guess)):
                print("you are MasterMind !")
                break
        if guess_chance == 0:
            print(f"Computer guessed no was {comp_guess}")
            break


output = MasterMind(5)
