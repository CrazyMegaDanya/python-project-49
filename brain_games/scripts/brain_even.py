import random
import prompt
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_count = 0
    while right_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer:")
        if answer == "yes" and number % 2 == 0:
            print('Correct!')
            right_count += 1
        elif answer == "no" and number % 2 != 0:
            print('Correct')
            right_count += 1
        elif answer == "yes" and number % 2 != 0:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return
        elif answer == "no" and number % 2 == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()