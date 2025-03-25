import random
import prompt
from brain_games.cli import welcome_user


def is_prime(number):
    if number <= 1:
        return "no"
    elif number == 2:
        return "yes"
    elif number % 2 == 0:
        return "no"
    for i in range(3, int((number**0.5) + 1), 2):
        if number % i == 0:
            return "no"
    return "yes"
    

def main():
    name = welcome_user()
    msg = (
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
    )
    print(msg)
    right_count = 0
    while right_count < 3:
        quest_number = random.randint(1, 100)
        print(f"Question: {quest_number}")
        answer = prompt.string("Your answer:")
        if answer == is_prime(quest_number):
            print("Correct!")
        elif answer == "yes" and is_prime(quest_number) == "no":
            msg = (
                "'yes' is wrong answer ;(. "
                "Correct answer was 'no'."
            )
            print(msg)
            print(f"Let's try again, {name}!")
            return
        elif answer == "no" and is_prime(quest_number) == "yes":
            msg = (
                "'no' is wrong answer "
                ";(. Correct answer was 'yes'."
            )
            print(msg)
            print(f"Let's try again, {name}!")
            return
        right_count += 1
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()