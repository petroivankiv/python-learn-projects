import re
from typing import Final
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        
def get_headless_browser():
    print('Starting up browser...')
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Prevents the browser from showing
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")

    return webdriver.Chrome(options=chrome_options)

        
def scrape_emails(browser, url: str) -> set:
    print(f'Scraping: "{url}" for emails')
    
    browser.get(url)
    page_source: str = browser.page_source
    list_of_emails: set = set()
    
    for re_match in re.finditer(EMAIL_REGEX, page_source):
        list_of_emails.add(re_match.group())

    return list_of_emails

def print_result(emails: set):
    for i, email in enumerate(emails, start=1):
        print(i, email, sep=': ')


def main():
    browser = get_headless_browser()
    emails: set = scrape_emails(browser, 'https://www.randomlists.com/email-addresses?qty=50')
    print_result(emails)


if __name__ == '__main__':
    main()
