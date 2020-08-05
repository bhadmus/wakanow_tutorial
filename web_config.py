from selenium import webdriver

class Driver:
    """
    This class will help us have an instance of our driver anywhere
    and save us the trouble of importing the webdriver from selenium,
    then instatiating the driver all over again
    """
    def __init__(self):
        self.driver = webdriver.Chrome()

    def launch_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()