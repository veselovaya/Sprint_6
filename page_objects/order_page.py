from selenium.webdriver import Keys

from page_objects.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import datetime
import allure


class OrderPage(BasePage):

    @allure.step('Ожидание загрузки окна "Для кого самокат"')
    def wait_for_loading_order_form(self):
        self.wait_visibility_element(OrderPageLocators.NAME_ORDER)

    @allure.step('Заполнить поле "Имя"')
    def fill_name_order(self, name):
        self.send_keys(OrderPageLocators.NAME_ORDER, name)

    @allure.step('Заполнить поле "Фамилия"')
    def fill_lastname_order(self, lastname):
        self.send_keys(OrderPageLocators.LASTNAME_ORDER, lastname)

    @allure.step('Заполнить поле "Адрес"')
    def fill_address_order(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_ORDER, address)

    @allure.step('Кликнуть на поле "Станция метро"')
    def click_metro_station(self):
        self.click_element(OrderPageLocators.METRO_ORDER)

    @allure.step('Выбрать станцию из списка')
    def choose_metro_station(self, metro):
        self.scroll_page(metro)
        self.wait_for_element_to_be_clickable(metro)
        self.click_element(metro)

    @allure.step('Заполнить поле "Телефон"')
    def fill_phone_order(self, phone):
        self.send_keys(OrderPageLocators.PHONE_ORDER, phone)

    @allure.step('Нажать на кнопку "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить форму "Для кого самокат"')
    def fill_user_data(self, name, lastname, address, metro, phone):
        self.fill_name_order(name)
        self.fill_lastname_order(lastname)
        self.fill_address_order(address)
        self.click_metro_station()
        self.choose_metro_station(metro)
        self.fill_phone_order(phone)

    @allure.step('Кликнуть на поле "Когда привезти самокат"')
    def click_order_date(self):
        self.click_element(OrderPageLocators.DATE_ORDER)

    @allure.step('Выбрать дату доставка')
    def choose_order_date(self):
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=1)
        formatted_date = future_date.strftime("%d.%m.%Y")
        self.send_keys(OrderPageLocators.DATE_ORDER, formatted_date)
        self.send_keys(OrderPageLocators.DATE_ORDER, Keys.ENTER)

    @allure.step('Выбрать срок аренды')
    def choose_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(period)

    @allure.step('Выбрать цвет самоката')
    def choose_color(self, color):
        self.click_element(color)

    @allure.step('Оставить комментарий к заказу')
    def comment_for_order(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_ORDER, comment)

    @allure.step('Нажать на кнопку "Заказать"')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Дождаться появления окна "Хотите оформить заказ?"')
    def wait_for_load_confirm_popup(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.CONFIRM_ORDER)

    @allure.step('Нажать "Да" в окне подтверждения заказа')
    def click_yes_confirm_popup(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER)

    @allure.step('Дождаться окна "Заказ оформлен"')
    def wait_for_order_inf_popup(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.CHECK_STATUS)

    @allure.step('Заполнить данные в форме "Про аренду"')
    def fill_order_data(self, period, color, comment):
        self.choose_order_date()
        self.choose_rental_period(period)
        self.choose_color(color)
        self.comment_for_order(comment)






