from random import randint

def roll_dice(amount: int = 2) -> list[int]:
  if amount <= 0:
    raise ValueError
  
  rolls: list[int] = []
  
  for i in range(amount):
    rolls.append(randint(1, 6));
    
  return rolls;

def main():
  while True:
    try:
      user_input: str = input("Задайте число: ")
      
      if user_input.lower() == 'exit':
        print('Дякую за гру!')
        break
      
      print(roll_dice(int(user_input)))
      
    except ValueError:
      print('Не правильне число')
      
      
if __name__ == '__main__':
  main()
      
  
