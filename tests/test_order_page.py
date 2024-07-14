import pytest
from locators.main_page_locators import MainPageLocators
from testdata import OrderData
from locators.order_page_locators import OrderPageLocators
from page_objects.order_page import OrderPage
from page_objects.main_page import MainPage
import allure


class TestOrderPage:
    @pytest.mark.parametrize(
        'order_button, user, metro_station, rental_period, color',
        [
            [MainPageLocators.ORDER_BUTTON_HEADER, OrderData.order_1, OrderPageLocators.METRO_BULVAR_STATION, OrderPageLocators.ONE_DAY_RENTAL,OrderPageLocators.GREY_COLOR],
            [MainPageLocators.ORDER_BUTTON_MAIN_PAGE, OrderData.order_2, OrderPageLocators.METRO_CHERKIZOVSKAYA, OrderPageLocators.TWO_DAYS_RENTAL, OrderPageLocators.BLACK_COLOR]
        ]
        )
    @allure.title('Тест заказа доставки самоката')
    @allure.description('При клике на кнопки "Заказать" и заполнении формы валидными данными появляется окно "Посмотреть статус"')
    def test_order_samokat_true(self, driver, order_button, user, metro_station, rental_period, color):

        main_page = MainPage(driver)
        main_page.click_cookie_button()
        main_page.click_element(order_button)

        order_page = OrderPage(driver)
        order_page.fill_user_data(user[0], user[1], user[2], metro_station, user[3])
        order_page.click_next_button()
        order_page.fill_order_data(rental_period, color, user[4])
        order_page.click_order_button()
        order_page.wait_for_load_confirm_popup()
        order_page.click_yes_confirm_popup()
        order_page.wait_for_order_inf_popup()

        button_text = order_page.get_actually_text(OrderPageLocators.CHECK_STATUS)
        assert button_text == 'Посмотреть статус'




