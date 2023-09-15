import random
import sys

class RPS:
    def __init__(self):
        print('Вітаю у грі RPS!')
        
        self.moves: dict = { 'rock': 'камінь', 'paper': 'папір', 'scissors': 'ножиці' }
        self.valid_moves: list[str] = list(self.moves.values())
        
    def play_game(self):
        user_move: str = input('Камінь, ножиці чи папір (для виходу з гри введіть - вийти)? >>>  ').lower()
        
        if user_move == 'вийти':
            print('Дякую за гру!')
            sys.exit()
        
        if user_move not in self.valid_moves:
            print('Задайте привильне слово')
            return self.play_game()
        
        ai_choice: str = random.choice(self.valid_moves)
        
        self.display_moves(user_move, ai_choice)
        self.check_move(user_move, ai_choice)
    
    def display_moves(self, user_move: str, ai_choice: str):
        print('---------')
        print(f'Ваш вибір: {user_move}')
        print(f'Вибір програми: {ai_choice}')
        print('---------')
    
    def check_move(self, user_move: str, ai_choice: str):
        if user_move == ai_choice:
            print('Нічия!')
        elif user_move == 'камінь' and ai_choice == 'ножиці':
            print('Ви перемогли')
        elif user_move == 'ножиці' and ai_choice == 'папір':
           print('Ви перемогли')
        elif user_move == 'папір' and ai_choice == 'камінь':
           print('Ви перемогли')
        else:
            print('Програма перемогла')
            
            
if __name__ == '__main__':
    rps = RPS()
    
    while True:
        rps.play_game()