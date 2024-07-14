from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.driver.find_element(*locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))


    def get_actually_text(self, locator):
        actuall = self.driver.find_element(*locator).text
        return actuall

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def wait_url_until_not_about_blank(self):
        WebDriverWait(self.driver, 5).until_not(EC.url_to_be('about:blank'))

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)