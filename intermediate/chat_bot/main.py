from difflib import get_close_matches
import json


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    
    if matches:
        return matches[0]
    
def chat_bot(knowledge: dict):
    while True:
        user_question: str = input('Ви: ')
        best_match: str | None = get_best_match(user_question, knowledge)
    
        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Бот: Я не знаю...')
        

if __name__ == '__main__':
    with open('intermediate/chat_bot/brain.json', 'r', encoding='utf-8') as f:
        brain: dict = json.load(f)
        chat_bot(brain)