import random
import prompt
from brain_games.cli import welcome_user
import math


def main():
    name = welcome_user()
    msg = ('Find the greatest common '
           'divisor of given numbers.'
    )
    print(msg)
    right_count = 0
    while right_count < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        print(f"Question: {first_number} {second_number}")
        user_answer = prompt.string("Your answer:") 
        correct_answer = math.gcd(first_number, second_number)
        if int(user_answer) == correct_answer:
            print('Correct!')
            right_count += 1
        else:
            msg = (f"'{user_answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'."
            )
            print(msg)
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()