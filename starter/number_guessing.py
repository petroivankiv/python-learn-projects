from random import randint

min_num, max_num = 1, 10
random_num: int = randint(min_num, max_num);

print(f"Вгадайте число від {min_num} до {max_num}");

while True:
  try:
    user_guess: int = int(input('Число: '))
  except ValueError as e:
    print('Введіть правильне число')
    continue
  
  if user_guess > random_num:
    print("Число є меншим");
    continue
    
  if user_guess < random_num:
    print("Число є більшим");
    continue
  
  print(f"Вітаю! Ви вгадали число {user_guess}.");
  break