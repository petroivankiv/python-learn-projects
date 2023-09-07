import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_sites(path: str) -> list[str]:
    sites: list[str] = []
    
    with open(path, 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            if 'https://' not in row[1] and 'http://' not in row[1]:
                sites.append(f'https://{row[1]}')
            else:
                sites.append(row[1]) 
        
        return sites
    

def get_user_agent():
    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            return f'({value} {value.name}) {value.description}'
        
    return f'(???????) Unknown status code'
    
    
    
def check_site(site: str, user_agent):
    try:
        code: int = requests.get(site, headers={'User-Agent': user_agent}).status_code
        print(site, get_status_description(code))
    except Exception:
        print(f'Немає інформації про веб сторінку - {site}')
        
        
def main():
    sites: list[str] = get_sites('starter/site_checker/sites.csv')
    agent = get_user_agent()
    
    for site in sites:
        check_site(site, agent)


if __name__ == "__main__":
    main()
       