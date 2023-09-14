from textblob import TextBlob
from dataclasses import dataclass
import sys


@dataclass
class Mood:
    emoji: str
    sentiment: float
    
def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity
    
    friendly_treshold: float = sensitivity
    hostile_treshold: float = -sensitivity
    
    if polarity >= friendly_treshold:
        return Mood('Чудово', polarity)
    elif polarity <= hostile_treshold:
        return Mood('Гнів', polarity)
    else:
        return Mood('Нормально', polarity)
    

def run_bot():
    print('Введіть деякий текс щоб визначити сентимент. Щоб вийти введіть - вийти')
    
    while True:
        user_input: str = input('Ви: ')
        
        if user_input == 'вийти':
            sys.exit()
        
        mood: Mood = get_mood(user_input, sensitivity=0.2)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')
        

if __name__ == '__main__':
    run_bot()
    