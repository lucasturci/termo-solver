from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Crawler:
    def __init__(self):
        # Launch the browser
        op = webdriver.ChromeOptions()
        op.add_argument('--headless')
        # Adding two lines below because driver crashes otherwise (see http://bit.ly/3lD6vfP)
        op.add_argument("--no-sandbox"); 
        op.add_argument("--disable-dev-shm-usage");
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
    
    def make_first_guess(self):
        self.driver.find_element(By.ID, 'help').click() # skip help page
        time.sleep(1)

        random_guess = 'termo'
        
        # Simulate key presses to send guess
        body = self.driver.find_element(By.CSS_SELECTOR, 'body')
        body.send_keys(random_guess)
        time.sleep(1)
        body.send_keys(Keys.ENTER)
        time.sleep(3)

    def get_termo_solution(self):
        # Navigate to the page that you want to read localStorage from
        self.driver.get('https://term.ooo')

        self.make_first_guess()

        # Execute a JavaScript code to read the localStorage
        solution = self.driver.execute_script('return JSON.parse(window.localStorage.getItem(\'termo\')).state[0].solution;')

        # Print the contents of the localStorage
        return solution

    def close(self):
        # Close the browser
        self.driver.quit()

# crawler = Crawler()
# print(crawler.get_termo_solution())
# crawler.close()