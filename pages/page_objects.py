from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from web_config import Driver

from file import ref


class GuestShopper:

    def __init__(self):
        self.site = Driver()

    def setup(self, url):
        self.site.launch_browser(url)

    def search_and_click(self, box, item, button):
        self.site.driver.find_element_by_css_selector(box).send_keys(item)
        self.site.driver.find_element_by_css_selector(button).click()

    def select_item(self, item):
        wait = WebDriverWait(self.site.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, item)))
        self.site.driver.find_element_by_css_selector(item).click()

    def scroll_page(self):
        self.site.driver.execute_script("window.scrollTo(0,500);")

    def add_to_cart(self, add):
        wait = WebDriverWait(self.site.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, add)))
        self.site.driver.find_element_by_css_selector(add).click()

    def buy_option(self):
        wait = WebDriverWait(self.site.driver, 15)
        wait.until(EC.visibility_of_element_located((By.ID, ref.amazon_buy_button)))
        self.site.driver.find_element_by_id(ref.amazon_buy_button).click()

    def proceed_to_checkout(self, button):
        wait = WebDriverWait(self.site.driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, button)))
        self.site.driver.find_element_by_css_selector(button).click()

    def verify_page(self, word):
        title = self.site.driver.title
        try:
            assert word in title
            print('Assertion Passed')
        except AssertionError:
            "Text not Found"
            print('Assertion Failed')
        # self.site.quit()
