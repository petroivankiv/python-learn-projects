from typing import Final
import requests
from os import getenv
from dotenv import load_dotenv, find_dotenv

# find the .env file and load it 
load_dotenv(find_dotenv())

API_KEY: Final[str] = getenv("CUTT_LY_API_KEY")
BASE_URL: Final[str] = ' https://cutt.ly/api/api.php'


def shorten_url(full_ulr: str):
    payload:dict = { 'key': API_KEY, 'short': full_ulr }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()
    
    if url_data:= data.get('url'):
        if url_data['status'] == 7:
            short_link = url_data['shortLink']
            
            print('Посилання: ', short_link)
        else:
            print('Статус помилки: ', url_data['status'])    
            
            
            
def main():
    input_link = input('Задайте посилання: ')
    shorten_url(input_link)
    

if __name__ == '__main__':
    main()
    
