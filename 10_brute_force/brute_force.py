import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open('starter/brute_force/words.text', 'r') as f:
        words: list[str] = f.read().splitlines()
        
    for i, match in enumerate(words, start=1):
        if match == word:
            print(f'Співпадіння: {word} (#{i})')
            
            
def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase
    
    if digits:
        chars += string.digits
        
    if symbols:
        chars += string.punctuation
        
    attemts: int = 0;
    
    for guess in itertools.product(chars, repeat=length):
        attemts += 1
        guess: str = ''.join(guess)
        
        if guess == word:
            return f'"{word}" було зламано за {attemts:,} спроб'
        

def main():
    password: str = input('Задайте слово від 3 до 6 літер, цифр: ')
    
    start_time: float = time.perf_counter()
    
    if common_match := common_guess(password):
        print(common_match)
    else:
        for i in range(3, 6):
            if cracked := brute_force(password, length=i, digits=True, symbols=False):
                print(cracked)
                break
            else:
                print(f'Не знайдено для {i}')
        
    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 's')
            

if __name__ == '__main__':
    main()