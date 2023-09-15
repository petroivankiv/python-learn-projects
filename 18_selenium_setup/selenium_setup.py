import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# optional
class Browser:
    # path to driver (chromedriver)
    def __init__(self, driver: str):
        print('Починаємо...')
        
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
        
    def open_page(self, url: str):
        print(f'Відкриваю: {url}')
        self.browser.get(url)
        
    def close_browser(self):
        print('Закриваю бравзер...')
        self.browser.close()
        
        
if __name__ == '__main__':
    browser = webdriver.Chrome()
    
    browser.get('https://google.com')
    
    time.sleep(5)