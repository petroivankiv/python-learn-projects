from bs4 import BeautifulSoup
import requests
import csv
from fake_useragent import UserAgent


def get_resources():
    sites: dict = {}
    
    with open('24_headline_scraper/sites.csv', 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            data: dict = { 'tag': row[1], 'class': row[2] }
            
            if 'https://' not in row[0] and 'http://' not in row[0]:
                sites[f'https://{row[0]}'] = data
            else:
                sites[row[0]] = data
        
        return sites


def get_soup(site: str) -> BeautifulSoup:
    """Get the soup back from the website, mmm..."""

    # Make a request
    headers: dict = { 'User-Agent': UserAgent().chrome }
    request = requests.get(site, headers=headers)
    html: bytes = request.content

    # Create a soup, mmm...
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_content(element):
    content = element.contents[0]
    
    if 'contents' in content:
        return get_content(content)
    else:
        if 'lower' in content:
            return content.lower()
        else:
            # span element doesn't have contents but text
            return content.text.lower()
    


def get_headlines(soup: BeautifulSoup, tag: str) -> list[str]:
    """Scrape the headlines from the soup we provide"""

    headlines: set = set()

    # Finds all the headers
    # for h in soup.findAll('h3', class_= className):
    for h in soup.findAll(tag):
        headline: str = get_content(h)
        headlines.add(headline)
            

    return sorted(headlines)


def print_found_headlines(terms_found: int, term: str, found_list: list[str]):
    # Show the new list that contains the headlines if a term was found in them
    print('----------------------------------')
    
    if terms_found:
        print(f'"{term}" було згадано {terms_found} разів.')
        print('----------------------------------')

        for i, headline in enumerate(found_list, start=1):
            print(f'{i}: {headline.capitalize()}')
    else:
        print(f'Не знайдено заголовків, які містять: "{term}"')
        print('----------------------------------')


def check_headlines(headlines: list[str], term: str, site: str):
    """Check if a term is found in a headline"""

    term_list: list[str] = []
    terms_found: int = 0

    # Loop through the headlines to find the keyword
    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
        else:
            print(f'{i}: {headline.capitalize()}')

    print_found_headlines(terms_found=terms_found, term=term, found_list=term_list)


def main():
    # Get resourses with a classes
    resourses: dict = get_resources()
    print(resourses.keys())
    
     # Get the user input and check for headlines
    user_input: str = input('What term would you like to check for? >> ')
    
    for i, site in enumerate(resourses.keys(), start=1):
        print()
        print(f'-------- Шукаємо "{user_input}" у "{site}" --------')
        print()
        
        soup: BeautifulSoup = get_soup(site)
        headlines: list[str] = get_headlines(soup=soup, tag=resourses.get(site)['tag'])
        check_headlines(headlines, user_input, site)
    

if __name__ == '__main__':
    main()
