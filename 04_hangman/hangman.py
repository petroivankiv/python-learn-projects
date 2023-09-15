from random import choice

def run_game():
    word: str = choice(['україна', 'воїн', 'перемога'])
    
    user_name = input("Яке ваше ім'я? >> ")
    
    print(f'Вітаю у грі, {user_name}')
    print("Згідно правил ви маєте вгадати слово, вгадуючи букви")
    
    guessed = ''
    tries = 3

    while tries > 0:
        blanks: int = 0
        
        print('Слово: ', end='')
        
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1
           
        # add a blank line 
        print()
    
        if blanks == 0:
           print('Ви вгадали слово!');
           break
       
        guess: str = input('Задайте букву: ')
        
        if len(guess) > 1:
            print(f'Тільки одну букву дозволено')
            continue
        
        if guess in guessed:
            print(f'Ви вже використали цю букву: {guess}')
            continue
        
        if guess not in word:
            tries -= 1
            print(f'Ви помилились... Залишилось спроб: {tries}')
        else:
            guessed += guess
            
        if tries == 0:
            print('У вас більше немає спроб. Гра завершена!')
            break


if __name__ == '__main__':
    run_game()
    