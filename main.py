import random


def handman():


    wordlist = ['челик', 'квадрат', 'унитаз', 'бекон', 'близнецы', "домашка"]
    secret = random.choice(wordlist)
    guesses = ''
    turns = 10


    while turns > 0:
        print('Твоё слово:')
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end='')
            else:
                print('_', end=' ')
                missed += 1

        if missed == 0:
            print('\n ураураураура ты выиграл')
            break

        guess = input('\nназови букву')
        guesses += guess
        if guess not in secret:
            turns -= 1
            print('не угадал')
            print('\n', 'осталось попыток: ', turns)
            if turns == 0:
                print('ты проиграл, лол')
                print("попробовать снова?")
                ans = input()
                if ans == 'да':
                    handman()
                else:
                    break
print('привет! добро пожаловать в игру поле чудес!')
handman()
