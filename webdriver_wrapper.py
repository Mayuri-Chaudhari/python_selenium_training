import pytest
from selenium import webdriver

class AutomationWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(r"D:\Mine\Company\Tata Tech Mar 2025\HybridFramework\driver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()
