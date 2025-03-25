import random
import prompt
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    right_count = 0
    while right_count < 3:
        element_list = []
        first_element = random.randint(1, 20)
        step = random.randint(2, 5)
        hidden_element = random.randint(0, 9)
        for i in range(10):
            element_list.append(first_element + i * step)
        search_element = element_list[hidden_element]
        element_list[hidden_element] = '..'
        print('Question: ', *element_list)
        answer = prompt.string("Your answer: ")
        if int(answer) == search_element:
            print('Correct!')
            right_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{search_element}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()