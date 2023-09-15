import requests
import os


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
    
    for ext in extensions:
        if ext in image_url:
            return ext
        
def download_image(image_url: str, name: str, folder: str = None):
    if ext := get_extension(image_url):
        if folder:
            image_name = f'{folder}/{name}{ext}'
        else:
            image_name = f'{name}{ext}'
    else:
        print('Підберіть файл з іншим розширенням!')
    
    if os.path.isfile(image_name):
        raise Exception('Файл вже існує')
    
    
    try:
        image_content: bytes = requests.get(image_name).content
        
        with open(image_name, 'wb') as handler:
            handler.write(image_content)
            print(f'Завантажено успішно: "{image_name}"')
            
    except Exception as e:
        print(f'Помилка: {e}')
        

if __name__ == '__main__':
    input_url: str = input('Задайте посилання: ')
    input_name: str = input('Задайте назву: ')
    
    print('Завантаження...')
    
    download_image(input_url, name=input_name, folder='starter/image_downloader')
    