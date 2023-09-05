def get_input(text: str):
    return input(f"Задайте {text}:");

name = get_input('ваше ім\'я');
language = get_input('мову програмування');


story = f"""
  Привіт! Моє ім'я {name}. Це мій перший застосунок, написаний мовою програмування {language}.
""";

print(story);