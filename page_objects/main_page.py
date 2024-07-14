from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Нажать на "Вопросы о важном"')
    def click_faq(self,question): #Кликаем на вопрос FAQ
        self.click_element(question)


    @allure.step('Нажать на "Принять куки"')
    def click_cookie_button(self):
        self.click_element(MainPageLocators.COOKIE_BUTTON)


    @allure.step('Перейти на другую вкладку браузера')
    def change_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])





